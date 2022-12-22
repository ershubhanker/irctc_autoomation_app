// First Search Notification - only show on first address bar search

var promptMarket = chrome.i18n.getMessage("ExtnMarket");
var browserLanguage = (navigator.language || navigator.userLanguage).toLowerCase();

function firstSearchNotification(tabId, changeInfo) {
    if (changeInfo.url) {

        var pc = extractQueryString("pc", changeInfo.url);

        var formcode = extractQueryString("form", changeInfo.url);

        if (changeInfo.url.includes("&DPC")) {
            var dpc = extractQueryString("DPC", changeInfo.url);
            pc = pc + "&DPC=" + dpc;

        }
        var isBingExtensionSearch = changeInfo.url.includes("search?form=" + formcode + "&pc=" + pc + "&q=");
        if (isBingExtensionSearch) {

            chrome.storage.local.get({ showFirstSearchNotification: true }, (items) => {
                if (isBingExtensionSearch && items && items.showFirstSearchNotification) {
                    chrome.storage.local.set({ showFirstSearchNotification: false });
                    chrome.tabs.insertCSS(tabId, { file: "templates/firstSearchNotification-chrome.css" });
                    chrome.tabs.executeScript(tabId, { file: "scripts/injectFirstSearchNotification.js" });

                }
                else if (isBingExtensionSearch && items && !items.showFirstSearchNotification) {
                    chrome.tabs.onUpdated.removeListener(firstSearchNotification);
                }
            });
        }
    }
}

function extractQueryString(param, url) {
	param = param.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
	var p = (new RegExp("[\\?&]" + param + "=([^&#]*)")).exec(url);
	return (p === null) ? "" : p[1];
}

setTimeout(function () {
    if (navigator.language.length == 5) {
        if (localStorage["ChangeItback"] != "False") {          // only for new user		
            chrome.storage.local.get("showFirstSearchNotification", (items) => {     // to restrict 2nd search injection
                //console.log(items.showFirstSearchNotification);		
                if (!items && items.showFirstSearchNotification == null || items.showFirstSearchNotification == "" || items.showFirstSearchNotification == undefined) {
                    if (promptMarket == browserLanguage) {
                        chrome.tabs.onUpdated.addListener(firstSearchNotification);
                    }
                }

            });
        }
    }
    else {
        promptMkt = promptMarket.substring(0, 2);
        if (localStorage["ChangeItback"] != "False") {          // only for new user		
            chrome.storage.local.get("showFirstSearchNotification", (items) => {     // to restrict 2nd search injection
                console.log(items.showFirstSearchNotification);
                if (!items && items.showFirstSearchNotification == null || items.showFirstSearchNotification == "" || items.showFirstSearchNotification == undefined) {
                    if (promptMkt == browserLanguage) {
                        chrome.tabs.onUpdated.addListener(firstSearchNotification);
                    }
                }

            });
        }
    }
}, 200);

var externalCallback = null;
var notificationDismissed = false;
chrome.runtime.onMessage.addListener(
    function (request) {
        if (request == "notificationDismissed") {
            notificationDismissed = true;
            if (externalCallback) {
                externalCallback({ isEnabled: "true" });
            }
        }
        return true;
    }
);


chrome.runtime.onMessageExternal.addListener(
    function (request, sender, sendResponse) {
        const url = 'https://browserdefaults.microsoft.com/';
        if (sender && sender.url && sender.url.toLocaleLowerCase().includes(url) && request == "isExtensionEnabled") {
            if (notificationDismissed) {
                sendResponse({ isEnabled: "true" });
            }
            else {
                console.log("sendResponse:" + sendResponse);
                externalCallback = sendResponse;
            }
        }
        return true;
    }
);

