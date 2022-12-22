const CHANNEL = 'Channel';
const MACHINE_ID = 'MachineID';
const DPC = 'DPC';
const MARKET = 'Market';
const PARTNER_CODE = 'PartnerCode';

var bingUrl = "https://www.bing.com/";
var browserDefaultsUrl = "https://browserdefaults.microsoft.com/";
var chromeWS = "https://chrome.google.com/";
var feedbackFwlink = "https://go.microsoft.com/fwlink/?linkid=2138838";
var defaultPC = "U519";

var market = chrome.i18n.getMessage("ExtnMarket");
var extensionId = chrome.runtime.id;
var machineID = (localStorage.MachineID == undefined || localStorage.MachineID == "" || localStorage.MachineID == null) ? guid() : localStorage.MachineID;

//Sets '_NTPC' session cookies in bing.com domain whenever background.js gets executed
setTimeout(function () {

	chrome.cookies.set({
		url: bingUrl, domain: '.bing.com', name: '_NTPC', value: !localStorage["pc"] ? defaultPC : localStorage["pc"],sameSite:'no_restriction',secure:true }, function (cookie) {

	});


	if (!localStorage["isInstalled"]) {
		localStorage["isInstalled"] = "done";
		machineID = localStorage[MACHINE_ID];
		chrome.storage.local.set({"MigratedLocalStorage": true});
		SendPingDetails("1");
		console.log("Extension isInstalled");
	}

	var _dpc = localStorage["_dpc"] ? localStorage["_dpc"] : "organic";
	if (_dpc != undefined && _dpc != "" && _dpc != null) {
		chrome.cookies.set({ url: bingUrl, domain: '.bing.com', name: '_DPC', value: _dpc ,sameSite:'no_restriction',secure:true}, function (cookie) {
		});
	}

	//To redirect feedback page while uninstalling the extension
	var uninstallUrl = feedbackFwlink + "&extnID=" + extensionId + "&mkt=" + market + "&mid=" + machineID + "&br=gc";
	chrome.runtime.setUninstallURL(uninstallUrl);

}, 900);

setTimeout(function () {

	if (!localStorage["pc"]) {
		console.log("registry");		
		var iMachineId = "", iPC = "", iChannel = "registry", iMarket = "";

		// Fetching Machine Id, Partner Code, DPC and Channel details from browserdefaults.microsoft.com
		chrome.cookies.get({ url: browserDefaultsUrl, name: chrome.runtime.id }, function (cookie) {

			if (cookie) {
				var cookieValue = String(cookie.value).split('&');
				for (var i = 0; i < cookieValue.length; i++) {

					var cookieData = cookieValue[i].split('=');

					if (cookieData[0].toLocaleUpperCase() == "MI") {
						iMachineId = cookieData[1];
					}
					else if (cookieData[0].toLocaleUpperCase() == "CH") {
						iChannel = cookieData[1];
					}
					else if (cookieData[0].toLocaleUpperCase() == "PC") {
						iPC = cookieData[1];
					}
					else if (cookieData[0].toLocaleUpperCase() == "BM") {
						iMarket = cookieData[1];
					}
				}
				chrome.cookies.remove({ url: browserDefaultsUrl, name: chrome.runtime.id });
			}

		});

		setTimeout(function () {
			var installDetails = {};
			// Assign PC values
			if (iPC != "") {
				localStorage["pc"] = iPC;
				chrome.storage.local.set({ "qspc": iPC });
				installDetails[PARTNER_CODE] = iPC;
			}
			else {
				localStorage["pc"] = defaultPC;
				installDetails[PARTNER_CODE] = defaultPC;
			}

			// Assign MachineID
			if (iMachineId != "") {
				localStorage[MACHINE_ID] = iMachineId;
				installDetails[MACHINE_ID]= iMachineId;
			}

			// Assign Channel
			localStorage["channel"] = iChannel;
            installDetails[CHANNEL] = localStorage["channel"];
			// Assign Browser Market
			if (iMarket != "") {
				localStorage["bmkt"] = iMarket;
				installDetails[MARKET] = iMarket;
			}

			// Assign DPC
			if (iPC != "") {
				localStorage["_dpc"] = iPC + "_" + localStorage["channel"];
				installDetails[DPC] = iPC + "_" + localStorage["channel"];
			}
			else {
				localStorage["_dpc"] = localStorage["channel"];
				installDetails[DPC] = localStorage["channel"];
			}
            chrome.storage.local.set(installDetails);

		}, 100);

	}
}, 500);

chrome.runtime.onInstalled.addListener(function (details) {

	if (details.reason == 'install') {
		
		console.log("install");
		var iMachineId = "", iPC = "", iChannel = "organic", iMarket = "";

		// Fetching Machine Id, Partner Code, DPC and Channel details from browserdefaults.microsoft.com
		chrome.cookies.get({ url: browserDefaultsUrl, name: chrome.runtime.id }, function (cookie) {
			if (cookie) {

				var cookieValue = String(cookie.value).split('&');
				for (var i = 0; i < cookieValue.length; i++) {

					var cookieData = cookieValue[i].split('=');

					if (cookieData[0].toLocaleUpperCase() == "MI") {
						iMachineId = cookieData[1];
					}
					else if (cookieData[0].toLocaleUpperCase() == "CH") {
						iChannel = cookieData[1];
					}
					else if (cookieData[0].toLocaleUpperCase() == "PC") {
						iPC = cookieData[1];
					}
					else if (cookieData[0].toLocaleUpperCase() == "BM") {
						iMarket = cookieData[1];
					}
				}
				chrome.cookies.remove({ url: browserDefaultsUrl, name: chrome.runtime.id });
			}
		});

        // Fetching  __utmz cookie value from https://chrome.google.com/
        chrome.cookies.get({ url: chromeWS, name: '__utmz' }, function (cookie) {

            if (cookie) {
                var chromeWSChannel = getChromeWSChannel(cookie.value);
                if (chromeWSChannel != "") {
                    iChannel = chromeWSChannel;
                }
                chrome.cookies.remove({ url: chromeWS, name: '__utmz' });
            }
        });

		setTimeout(function () {
			var installDetails = {};
			// Assign PC values
			if (iPC != "") {
				localStorage["pc"] = iPC;
				chrome.storage.local.set({ "qspc": iPC });
				installDetails[PARTNER_CODE] = iPC;
			}
			else {
				localStorage["pc"] = defaultPC;
				installDetails[PARTNER_CODE] = defaultPC;
			}

			// Assign MachineID
			if (iMachineId != "") {
				localStorage[MACHINE_ID] = iMachineId;
				installDetails[MACHINE_ID]= iMachineId;
			}

			// Assign Channel
			localStorage["channel"] = iChannel;
            installDetails[CHANNEL] = localStorage["channel"];
			// Assign Browser Market
			if (iMarket != "") {
				localStorage["bmkt"] = iMarket;
				installDetails[MARKET] = iMarket;
			}

			// Assign DPC
			if (iPC != "") {
				localStorage["_dpc"] = iPC + "_" + localStorage["channel"];
				installDetails[DPC] = iPC + "_" + localStorage["channel"];
			}
			else {
				localStorage["_dpc"] = localStorage["channel"];
				installDetails[DPC] = localStorage["channel"];
			}
            chrome.storage.local.set(installDetails);

		}, 100);
		//To redirect Analytic redirection page while installing the extension
		setTimeout(function () {
			var redirectionURL = "https://go.microsoft.com/fwlink/?linkid=2128904&trackingid=" + chrome.runtime.id + "&partnercode=" + localStorage["pc"] + "&browser=gc" + "&mkt=" + market;

			if (localStorage["channel"] != undefined && localStorage["channel"] != "" && localStorage["channel"] != null) {
				redirectionURL += "&channel=" + localStorage["channel"];
			}

			if (localStorage[MACHINE_ID] != undefined && localStorage[MACHINE_ID] != "" && localStorage[MACHINE_ID] != null) {
				redirectionURL += "&machineid=" + localStorage[MACHINE_ID];
			}

			chrome.tabs.create({ url: redirectionURL });
		}, 600);

	
	}	
    else if (details.reason == 'update') {
        localStorage["ChangeItback"] = "False";		
        //Call for Update Ping	
		var installDetails = {};

        if (localStorage["_dpc"]) {
            installDetails[DPC] = localStorage["_dpc"];
        }
        if (localStorage[MACHINE_ID]) {
            installDetails[MACHINE_ID] = localStorage[MACHINE_ID];
        }
        if (localStorage["channel"]) {
            installDetails[CHANNEL] = localStorage["channel"];
        }
        if (localStorage["bmkt"]) {
            installDetails[MARKET] = localStorage["bmkt"];
        }
		if (localStorage["pc"]) {
            installDetails[PARTNER_CODE] = localStorage["pc"];
        }
        chrome.storage.local.set(installDetails);
        chrome.storage.local.set({"MigratedLocalStorage": true});
        SendPingDetails("3");	
    }	
});
chrome.tabs.onActivated.addListener(function () {
    if (localStorage.PingDate == "" || localStorage.PingDate != new Date().toDateString()) {
        //Call for Update Ping
        SendPingDetails("2");
        localStorage["PingDate"] = new Date().toDateString()
    }
});

/* Function to create an unique machine id */
function guid() {
    function s4() {
        return Math.floor((1 + Math.random()) * 0x10000)
            .toString(16)
            .substring(1);
    }
    var MachineGUID = s4() + s4() + s4() + s4() + s4() + s4() + s4() + s4();
    MachineGUID = MachineGUID.toLocaleUpperCase();
    localStorage[MACHINE_ID] = MachineGUID;
	chrome.storage.local.set({ 
        [MACHINE_ID]: MachineGUID
    });
    return MachineGUID;
}

function SendPingDetails(status) {

	var manifestData = chrome.runtime.getManifest();
	var extensionVersion = manifestData.version;
	var startIndex = navigator.userAgent.indexOf("(");
	var endIndex = navigator.userAgent.indexOf(")");
	var OS = navigator.userAgent.substring(startIndex + 1, endIndex).replace(/\s/g, '');
	var browserLanguage = (localStorage["bmkt"]) ? localStorage["bmkt"] : navigator.language;

	var extensionName = manifestData.name.replace(/ /g, "").replace('&', 'and');

	var browserVersion = navigator.userAgent.substr(navigator.userAgent.indexOf("Chrome")).split(" ")[0].replace("/", "");

	setTimeout(function () {
		var pc = (localStorage.pc == undefined || localStorage.pc == "" || localStorage.pc == null) ? "U519" : localStorage.pc;
		var pingURL = 'http://g.ceipmsn.com/8SE/44?';
		var tVData = 'TV=is' + pc + '|pk' + extensionName + '|tm' + browserLanguage + '|bv' + browserVersion + '|ex' + extensionId + '|es' + status;
		if (localStorage["channel"])
			tVData = tVData + "|ch" + localStorage["channel"];
		if (localStorage["_dpc"])
			tVData = tVData + "|dp" + localStorage["_dpc"];
		pingURL = pingURL + 'MI=' + machineID + '&LV=' + extensionVersion + '&OS=' + OS + '&TE=37&' + tVData;
		pingURL = encodeURI(pingURL);  // For HTML Encoding
		var xhr = new XMLHttpRequest();
		xhr.open("GET", pingURL, true);
		xhr.send();
	}, 500);
};

function getChromeWSChannel(cookieValue) {

    // Sample Chrome Webstore PaidAds cookie Value: 73091649.1608191832.10.6.utmcsr=bgads|utmccn=rwdsus|utmcmd=(not%20set)
	//Cookie value: 73091649.1614306380.141.5.utmcsr=bgads|utmccn=rwdsus|utmcmd=rwdmed|utmcct=rwdcon
	//DPC: source_medium_campaign_content (bgads_rwdmed_rwdsus_rwdcon)
    var strSource = "";
    var strCampaign = "";
	var strMedium = "";
	var strContent = "";
    var strWSChannel = "";
    var splitStr = cookieValue.split(".");

    if (splitStr[splitStr.length - 1] != "") {
        var utmValues = splitStr[splitStr.length - 1].split("|");

        for (i = 0; i < utmValues.length; i++) {
            var utmValue = utmValues[i].split("=");
            if (utmValue[0] == "utmcsr") {
                strSource = utmValue[1];
            }
            else if (utmValue[0] == "utmccn") {
                strCampaign = utmValue[1];
            }
			 else if (utmValue[0] == "utmcmd") {
                strMedium = utmValue[1];
            }
			 else if (utmValue[0] == "utmcct") {
                strContent = utmValue[1];
            }
        }

        if (strSource == "bgads") {
			
            strWSChannel = strSource;
			
			if (strMedium != "(not%20set)" && strMedium != "(direct)" && strMedium != "(organic)") {
				strWSChannel = strWSChannel + "_" + strMedium ;
            }
			
            if (strCampaign != "(not%20set)" && strCampaign != "(direct)" && strCampaign != "(organic)") {
				strWSChannel = strWSChannel  + "_" + strCampaign ;
            }
			
			 if (strContent != "(not%20set)" && strContent != "(direct)" && strContent != "(organic)" && strContent !="") {
				strWSChannel = strWSChannel + "_" + strContent;
            }
        }

        return strWSChannel;
    }
}

function extractQueryString(param, url) {
	param = param.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
	var p = (new RegExp("[\\?&]" + param + "=([^&#]*)")).exec(url);
	return (p === null) ? "" : p[1];
}

chrome.browserAction.onClicked.addListener(function (tab) {
	var redirectURL = "https://www.msn.com/?pc=" + defaultPC + "&ocid=MSNHP_" + defaultPC;
	if (localStorage["pc"]) {
		redirectURL = "https://www.msn.com/?pc=" + localStorage["pc"] + "&ocid=MSNHP_" + localStorage["pc"];
	}
	chrome.tabs.create({ url: redirectURL });
});

chrome.webRequest.onBeforeRequest.addListener(function (details) {

    function getSearchUrl(queryString, pc) {
        return "https://www.bing.com/search?form=BGGCDF&pc=" + pc + "&q=" + queryString;
	}
	function getHomepageUrl(pc) {
		return "https://www.msn.com/?pc=" + pc + "&ocid=MSNHP_" + pc;
	}

	var partnerCode = extractQueryString("pc", details.url);
	var formCode = extractQueryString("form", details.url);
	var queryString = extractQueryString("q", details.url);


	if (localStorage["pc"]) {
		partnerCode = localStorage["pc"];
	}

	var URL = getHomepageUrl(partnerCode);
    if (formCode != "") {
		URL = getSearchUrl(queryString, partnerCode);
	}

	return {
		redirectUrl: URL
	};
}, {
	urls: ["*://www.bing.com/search?form=BGGCMF&pc=U519*","*://www.msn.com/?pc=U519&osmkt=*"] // List of URLs

}, ["blocking"]);// Block intercepted requests until this handler has finished

chrome.runtime.onMessage.addListener(function (msg) {
	if (msg == "setMachineID") {
		chrome.cookies.set({ url: browserDefaultsUrl, domain: '.browserdefaults.microsoft.com', name: 'MachineID', value: localStorage[MACHINE_ID], sameSite: 'no_restriction', secure: true }, function (cookie) {

        });
	}
});

