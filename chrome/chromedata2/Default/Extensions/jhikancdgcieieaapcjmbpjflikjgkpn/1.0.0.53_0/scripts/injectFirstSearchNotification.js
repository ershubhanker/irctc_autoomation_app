var promptMarket = chrome.i18n.getMessage("ExtnMarket");
var version=chrome.runtime.getManifest().version;
console.log("version:"+version);
var linkid = "2179704";
var xid = "107";
chrome.runtime.sendMessage("setMachineID");

var notificationFrame = document.createElement("iframe");

var listenerRef = function clickListener() {
    window.removeEventListener("focus", listenerRef);
    window.removeEventListener("click", listenerRef);
    try {
        chrome.runtime.sendMessage("notificationDismissed");
    }
    catch (exception) {
        console.log("Extension disabled");
        notificationFrame.classList.remove("b_hide");
    }
}


if (!document.hasFocus()) {

    var body = document.querySelector("body");
    notificationFrame.id = "ChangeItBack";
    notificationFrame.classList.add("changeItBack");
    notificationFrame.src = "https://go.microsoft.com/fwlink/?linkid=" + linkid + "&xid=" + xid + "&version=" + version + "&bmkt=" + promptMarket;
    body.appendChild(notificationFrame);
    notificationFrame.classList.add("b_hide");

    window.addEventListener("click", listenerRef);
    window.addEventListener("focus", listenerRef);

}
