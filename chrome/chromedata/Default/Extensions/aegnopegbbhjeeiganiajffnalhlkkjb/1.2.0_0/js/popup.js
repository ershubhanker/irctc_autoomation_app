
    
    let browserEnvironment = new systemUtil.browserEnvironmentData();
    let hasLicense = false;
    let partnerId = 'ut';
    let torrentArray = [];
    let numTorrentDisplayForFreeUser = 5;
    let numTorrents = 0;
    let currentUrl = window.location.href;

    // Create all elements
    let linkStyle = document.createElement('link');
    linkStyle.setAttribute('rel', 'stylesheet');
    linkStyle.setAttribute('href', chrome.runtime.getURL("../css/custom.css"));

    let popup = document.createElement('div');
    popup.setAttribute('id', 'torrent-scanner-popup');
    popup.setAttribute('style', 'display: none;');

    let xclose = document.createElement('div');
    xclose.setAttribute('id', 'ys-bt-x-close');
    xclose.setAttribute('class', 'x-close');
    xclose.appendChild(document.createTextNode("✖"));

    let wrapper = document.createElement('div');
    wrapper.setAttribute('id', 'yf-bt-wrapper');

    // Header section
    let header = document.createElement('div');
    header.setAttribute('class', 'header');
    let logo = document.createElement('img');
    logo.setAttribute('class', 'sts-logo');
    let upgradeToProBtn = document.createElement('button');
    upgradeToProBtn.setAttribute('id', 'upgrade-to-pro');
    upgradeToProBtn.setAttribute('class', 'upgrade-to-pro');
    upgradeToProBtn.appendChild(document.createTextNode('Activate License Key'));
    let refreshBtn = document.createElement('button');
    refreshBtn.setAttribute('id', 'refresh');
    refreshBtn.setAttribute('class', 'refresh');
    refreshBtn.appendChild(document.createTextNode('Refresh'));
    refreshBtn.setAttribute('class', 'display-none');
    let settingsBtn = document.createElement('button');
    settingsBtn.setAttribute('id', 'settings');
    settingsBtn.setAttribute('class', 'settings');
    let settingsImg = document.createElement('img');
    settingsImg.setAttribute('src', chrome.runtime.getURL('../img/popup/setting-icon.svg'));

    settingsBtn.appendChild(settingsImg);
    header.append(logo, upgradeToProBtn, refreshBtn, settingsBtn);
    // End header section

    // Content section
    let container = document.createElement('div');
    container.setAttribute('class', 'container');

    let searchContent = document.createElement('div');
    searchContent.setAttribute('class', 'search-content');
    let searchInput = document.createElement('input');
    searchInput.setAttribute('id', 'search-input');
    searchInput.setAttribute('class', 'search-input');
    searchInput.setAttribute('type', 'search');
    searchInput.setAttribute('placeholder', 'Search the web');

    let searchBtn = document.createElement('span');
    searchBtn.setAttribute('id', 'search-btn');
    searchBtn.setAttribute('class', 'search-btn');

    searchContent.append(searchInput, searchBtn);

    let mainContainer = document.createElement('div');
    mainContainer.setAttribute('class', 'main-container');

    let torrentContainer = document.createElement('div');
    torrentContainer.setAttribute('id', 'torrent-data');
    torrentContainer.setAttribute('class', 'torrent-content');

    let checkSection = document.createElement('div');
    checkSection.setAttribute('id', 'checked-sites');
    checkSection.setAttribute('class', 'checked-sites-section');
    let checkLeft = document.createElement('div');
    checkLeft.setAttribute('class', 'left');
    checkLeft.appendChild(document.createTextNode('Checked Sites'));
    let checkRight = document.createElement('div');
    checkRight.setAttribute('class', 'right');
    let maliciousCount = document.createElement('span');
    maliciousCount.setAttribute('id', 'mal-count');
    maliciousCount.setAttribute('class', 'mal-count');
    maliciousCount.appendChild(document.createTextNode('0'));

    checkRight.append(maliciousCount);
    checkSection.append(checkLeft, checkRight);

    let torrentTable = document.createElement('div');
    torrentTable.setAttribute('class', 't-table');
    let torrentTableHeader = document.createElement('div');
    torrentTableHeader.setAttribute('class', 't-header');
    let torrentTableName = document.createElement('div');
    torrentTableName.setAttribute('class', 't-name');
    torrentTableName.appendChild(document.createTextNode('Torrent Name'));
    let torrentTableStatus = document.createElement('div');
    torrentTableStatus.setAttribute('class', 't-status');
    torrentTableStatus.appendChild(document.createTextNode('Status'));
    let torrentTableQuality = document.createElement('div');
    torrentTableQuality.setAttribute('class', 't-quality');
    torrentTableQuality.appendChild(document.createTextNode('Quality'));
    let torrentTableLang = document.createElement('div');
    torrentTableLang.setAttribute('class', 't-lang');
    torrentTableLang.appendChild(document.createTextNode('Lang.'));
    let torrentTableMore = document.createElement('div');
    torrentTableMore.setAttribute('class', 't-more');
    torrentTableMore.appendChild(document.createTextNode(''));

    torrentTableHeader.append(torrentTableName, torrentTableStatus, torrentTableQuality, torrentTableLang, torrentTableMore);

    let torrentTableBody = document.createElement('div');
    torrentTableBody.setAttribute('id', 'table-body');
    torrentTableBody.setAttribute('class', 't-body');

    let loadingContainer = document.createElement('div');
    loadingContainer.setAttribute('id', 'loading');
    loadingContainer.setAttribute('class', 'spinner');
    let bounce1 = document.createElement('div');
    bounce1.setAttribute('class', 'bounce1');
    let bounce2 = document.createElement('div');
    bounce2.setAttribute('class', 'bounce2');
    let bounce3 = document.createElement('div');
    bounce3.setAttribute('class', 'bounce3');

    loadingContainer.append(bounce1, bounce2, bounce3);

    torrentTable.append(torrentTableHeader, torrentTableBody, loadingContainer);
    torrentContainer.append(checkSection, torrentTable);
    mainContainer.append(torrentContainer);
    container.append(searchContent, mainContainer);
    // End content section

    // Footer section
    let footer = document.createElement('div');
    footer.setAttribute('class', 'footer');
    let footerContent = document.createElement('span');
    let torrentNum = document.createElement('span');
    torrentNum.setAttribute('id', 'numberScanned');
    torrentNum.setAttribute('class', 'numberScanned');
    torrentNum.appendChild(document.createTextNode('0'));
    let feedbackBtn = document.createElement('a');
    feedbackBtn.setAttribute('id', 'feedbackButton');
    feedbackBtn.setAttribute('class', 'feedbackButton');
    feedbackBtn.appendChild(document.createTextNode('Leave feedback'));

    footerContent.append(torrentNum, document.createTextNode(' scanned torrents'));
    footer.append(footerContent, feedbackBtn);
    // End footer section

    // Settings popup
    let settingWrapper = document.createElement('div');
    settingWrapper.setAttribute('id', 'ys-bt-setting-wrapper');
    settingWrapper.setAttribute('class', 'setting-wrapper');
    let settingLogo = document.createElement('img');
    settingLogo.setAttribute('class', 'sts-logo');
    let settingContainer = document.createElement('div');
    settingContainer.setAttribute('id', 'pro-container');
    settingContainer.setAttribute('class', 'setting-container');
    let settingBack = document.createElement('div');
    settingBack.setAttribute('id', 'previous');
    settingBack.setAttribute('class', 'previous');
    settingBack.appendChild(document.createTextNode('Back'));
    let settingLicenseContent = document.createElement('div');
    settingLicenseContent.setAttribute('id', 'activate-license');
    settingLicenseContent.setAttribute('class', 'license-content');
    let licenseP = document.createElement('p');
    licenseP.appendChild(document.createTextNode('Enter your license key and click on the activate button to start using '));
    let licenseSpan = document.createElement('span');
    licenseSpan.setAttribute('id', 'proTitle');
    licenseSpan.appendChild(document.createTextNode('µTorrent Web Pro'));
    licenseP.appendChild(licenseSpan);
    let licenseInput = document.createElement('input');
    licenseInput.setAttribute('type', 'text');
    licenseInput.setAttribute('id', 'license-key');
    licenseInput.setAttribute('class', 'license-key-input');
    let licenseButton = document.createElement('button');
    licenseButton.setAttribute('id', 'activate-license-button');
    licenseButton.setAttribute('class', 'activate-license-button');
    licenseButton.appendChild(document.createTextNode('Activate'));
    let hr1 = document.createElement('hr');
    hr1.setAttribute('style', 'margin-top: 15px');
    let hr2 = document.createElement('hr');
    hr2.setAttribute('style', 'margin-top: 15px');
    let settingBuyContent = document.createElement('div');
    settingBuyContent.setAttribute('id', 'buy-pro');
    let buyP = document.createElement('p');
    buyP.appendChild(document.createTextNode('If you do not have a license key, click on the button below to purchase one'));
    let buyButton = document.createElement('button');
    buyButton.setAttribute('id', 'purchase-pro');
    buyButton.setAttribute('class', 'buy-button');
    buyButton.appendChild(document.createTextNode('Purchase License Key'));
    let nativeMessagingButton = document.createElement('button');
    nativeMessagingButton.setAttribute('id', 'allow-native-messaging');
    nativeMessagingButton.setAttribute('class', 'allow-native-messaging');
    nativeMessagingButton.appendChild(document.createTextNode('Allow communication with Softwares'));
    let settingFeedbackButton = document.createElement('button');
    settingFeedbackButton.setAttribute('class', 'feedbackButton');
    settingFeedbackButton.appendChild(document.createTextNode('Leave feedback'));

    settingLicenseContent.append(licenseP, licenseInput, licenseButton, hr1);
    settingBuyContent.append(buyP, buyButton, hr2);
    settingContainer.append(settingBack, settingLicenseContent, settingBuyContent, nativeMessagingButton, settingFeedbackButton);
    settingWrapper.append(settingLogo, settingContainer);
    // End settings popup

    wrapper.append(header, container, footer);
    document.body.appendChild(popup);

    let shadow = popup.attachShadow({ mode: 'open' });
    shadow.append(xclose, linkStyle, wrapper, settingWrapper);

    // Close button clicked, close popup
    xclose.addEventListener('click', () => {
        popup.style.display = "none";
    });

    // Setting button clicked
    settingsBtn.addEventListener('click', () => { 
        settingWrapper.style.display = 'block';
        wrapper.style.display = 'none';
    });

    settingBack.addEventListener('click', () => {
        wrapper.style.display = 'block';
        settingWrapper.style.display = 'none';
    });

    // document body clicked
    document.body.addEventListener('click', (ev) => {
        if (ev.target?.id !== "torrent-scanner-popup") {
            popup.style.display = 'none';
        }
    });

    // upgrade to pro button clicked
    upgradeToProBtn.addEventListener('click', () => {
        settingWrapper.style.display = 'block';
        wrapper.style.display = 'none';

        chrome.runtime.sendMessage({
            what: 'eventType',
            name: 'UpgradetoProButton',
            clicked: 'button'
        });
    });

    searchInput.addEventListener('keypress', (event) => {
        let torrentWord = 'torrent';
        if (searchInput.value.indexOf(torrentWord) !== -1) {
            torrentWord = '';
        }
        if (event.key === "Enter") {
            if (browserEnvironment.BrowserFamily == "Opera") {
                window.open('https://www.google.com/search?q=' + searchInput.value + ' ' + torrentWord + "&client=opera&sourceid=opera&ie=UTF-8&oe=UTF-8", '_top');
            } else {
                window.open('https://www.google.com/search?q=' + searchInput.value + ' ' + torrentWord, '_top');
            }
        }

        chrome.runtime.sendMessage({
            what: 'popupSearchBar',
            fromPopUI: true,
            searchEngine: "google",
            searchQuery: searchInput.value
        });
    });

    searchBtn.addEventListener('click', () => {
        let torrentWord = 'torrent';
        if (searchInput.value.indexOf(torrentWord) !== -1) {
            torrentWord = '';
        }
        if (browserEnvironment.BrowserFamily == "Opera") {
            window.open('https://www.google.com/search?q=' + searchInput.value + ' ' + torrentWord + "&client=opera&sourceid=opera&ie=UTF-8&oe=UTF-8", '_top');
        } else {
            window.open('https://www.google.com/search?q=' + searchInput.value + ' ' + torrentWord, '_top');
        }

        chrome.runtime.sendMessage({
            what: 'popupSearchBar',
            fromPopUI: true,
            searchEngine: "google",
            searchQuery: searchInput.value
        });
    }); 

    feedbackBtn.addEventListener('click', () => {
        if (hasLicense) {
            window.open("https://www.surveymonkey.com/r/MGSXQTF", "_blank");
        } else {
            window.open("https://www.surveymonkey.com/r/CP5JWBC", "_blank");
        }

        chrome.runtime.sendMessage({
            what: 'eventType',
            name: 'FeedbackButton',
            clicked: 'button'
        });
    });

    settingFeedbackButton.addEventListener('click', () => {
        if (hasLicense) {
            window.open("https://www.surveymonkey.com/r/MGSXQTF", "_blank");
        } else {
            window.open("https://www.surveymonkey.com/r/CP5JWBC", "_blank");
        }

        chrome.runtime.sendMessage({
            what: 'eventType',
            name: 'FeedbackButton',
            clicked: 'button'
        });
    });

    // Activate license trigger
    licenseButton.addEventListener('click', () => {
        let licenseKey = licenseInput.value || '';

        chrome.runtime.sendMessage({what: "activateLicense", data: { licenseKey: licenseKey }}, (response) => {
            if (response.request) {
                // reload page
                window.location.reload();
            } else {
                licenseInput.value = '';
                licenseInput.placeholder = 'Invalid License Key, try again.';
            }
        });

        chrome.runtime.sendMessage({
            what: 'eventType',
            name: 'ActivateButton',
            clicked: 'button'
        });
    });

    // Buy button clicked
    buyButton.addEventListener('click', () => {
        chrome.storage.local.get({ 'b' : null }, (data) => {
            if (data.b == "bt") {
                if (browserEnvironment.BrowserFamily == "Opera") {
                    window.open("https://gateway.lavasoft.com/ext/buy/bittorrentpro/?mkey7=Opera", "_blank");
                } else if (browserEnvironment.BrowserFamily == "Edge") {
                    window.open("https://gateway.lavasoft.com/ext/buy/bittorrentpro/?mkey7=EDGE ", "_blank");
                } else {
                    window.open("https://gateway.lavasoft.com/ext/buy/bittorrentpro/", "_blank");
                }
            } else if (data.b == "ut") {
                if (browserEnvironment.BrowserFamily == "Opera") {
                    window.open("https://gateway.lavasoft.com/ext/buy/utorrentpro/?mkey7=Opera", "_blank");
                } else if (browserEnvironment.BrowserFamily == "Edge") {
                    window.open("https://gateway.lavasoft.com/ext/buy/utorrentpro/?mkey7=EDGE", "_blank");
                } else {
                    window.open("https://gateway.lavasoft.com/ext/buy/utorrentpro/", "_blank");
                }
            } else {
                if (browserEnvironment.BrowserFamily == "Opera") {
                    window.open("https://gateway.lavasoft.com/ext/buy/utorrentpro/?mkey7=Opera", "_blank");
                } else if (browserEnvironment.BrowserFamily == "Edge") {
                    window.open("https://gateway.lavasoft.com/ext/buy/utorrentpro/?mkey7=EDGE", "_blank");
                } else {
                    window.open("https://gateway.lavasoft.com/ext/buy/utorrentpro/", "_blank");
                }
            }
        });

        chrome.runtime.sendMessage({
            what: 'eventType',
            name: 'PurchaseLicenseButton',
            clicked: 'button'
        });
    });

    const createPermissionBanner = () => {
        let permissionPanel = document.createElement("div");
        permissionPanel.setAttribute("id", "ys-bt-permission-banner");
        let containerPermission = document.createElement('div');
        containerPermission.setAttribute("class", "container");
        let perImg = document.createElement("img");
        perImg.setAttribute("class", "per-img");
        perImg.setAttribute("src", "data:image/svg+xml;base64,PHN2ZyBpZD0iaWNvbi1sb29wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDIiIGhlaWdodD0iMTAyIiB2aWV3Qm94PSIwIDAgMTAyIDEwMiI+CiAgPGcgaWQ9Il8yNDI3MDgyNjQiPgogICAgPHJlY3QgaWQ9Il8yNDI3MDc5NTIiIHdpZHRoPSIxMDIiIGhlaWdodD0iMTAyIiBmaWxsPSJub25lIi8+CiAgICA8cmVjdCBpZD0iXzI0MjcwNzgzMiIgd2lkdGg9Ijc2LjUiIGhlaWdodD0iNzYuNSIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTIuNzUgMTIuNzUpIiBmaWxsPSJub25lIi8+CiAgPC9nPgogIDxwYXRoIGlkPSJQYXRoXzc0MCIgZGF0YS1uYW1lPSJQYXRoIDc0MCIgZD0iTTMuODcxLDI1LjY4QTMwLjgyMywzMC44MjMsMCwwLDAsMjcuNDE1LDIzLjMsMzAuODA5LDMwLjgwOSwwLDAsMCw0Mi4zNjgsNC45NjdjLjAyNS0uMDg0LjA2Ni0uMjIzLjExOS0uNDEycy4wOTEtLjMyLjExNC0uNDA1bDQuNjEzLDEuMjMzYy0uMDU3LjIxLS4xLjM2OS0uMTMyLjQ4cy0uMDc2LjI2LS4xMzguNDY4QTM1LjU4MSwzNS41ODEsMCwwLDEsMjkuNjc1LDI3LjUsMzUuNTY4LDM1LjU2OCwwLDAsMSwyLjUwNywzMC4yNTZMMy44NzEsMjUuNjhaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzNC45NTcgNTcuODU0KSIgZmlsbD0iIzdjYjM0MiIvPgogIDxwYXRoIGlkPSJQYXRoXzc0MSIgZGF0YS1uYW1lPSJQYXRoIDc0MSIgZD0iTTExLjQ0LDUzLjI1N2gwbDAsMGEzNS42ODksMzUuNjg5LDAsMCwxLS4wMTktNTAuNDU4VjIuNzg1aDBsMCwwcS4xODMtLjE4My4zNDItLjMzOGMuMTMyLS4xMjkuMjQ2LS4yMzguMzQyLS4zMjlMMTUuNCw1LjU3N2MtLjEyMS4xMTQtLjIyMy4yMTItLjMuMjkycS0uMTU5LjE1NS0uMjkxLjI4N3YuMDA5aDBsMCwwYTMwLjkwOSwzMC45MDksMCwwLDAsLjAxLDQzLjcxNmguMDA5bC0xLjcxMSwxLjcxMS0xLjY2LDEuNjY5LDAsMCwwLDBaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMy43NzggMjkuNTc4KSIgZmlsbD0iIzdjYjM0MiIvPgogIDxwYXRoIGlkPSJQYXRoXzc0MiIgZGF0YS1uYW1lPSJQYXRoIDc0MiIgZD0iTTE4Ljk3NCwxOC41NjhsLTMuMzEyLTguM0w2LjU0LDE0LjM3Niw0LjU3OSwxMC4wMjRsMTEuMzktNS4xMzEsMi4yNjgtMS4wMjIuOTI1LDIuMzJMMjMuNCwxNi44MTJaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2My44MzQgNTMuOTYyKSIgZmlsbD0iIzY4OWYzOCIvPgogIDxwYXRoIGlkPSJQYXRoXzc0MyIgZGF0YS1uYW1lPSJQYXRoIDc0MyIgZD0iTTEuMTMsMy41NDYsMTIuNDkxLDIuMjM5bDIuNDc2LS4yODUuMTc2LDIuNDg5TDE2LjAyNywxNi45bC00Ljc2My4zMzYtLjcwNy05Ljk3M0wxLjY3Miw4LjI4OVoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE1Ljc1NCAyNy4yMzkpIiBmaWxsPSIjNjg5ZjM4Ii8+CiAgPHBhdGggaWQ9IlBhdGhfNzQ0IiBkYXRhLW5hbWU9IlBhdGggNzQ0IiBkPSJNNDUuNjQxLDMwLjczM0g0My4yNWwtMi4zNDMuNDQ4QTMwLjksMzAuOSwwLDAsMCw0LjczMSw2LjYzNmgwbC0uNDQ5LjA4Ni0uNDM4LjA5MkwyLjgxNywyLjE2M3EuMzQzLS4wNzYuNTEzLS4xMTFsLjUtLjFoMGEzNS43LDM1LjcsMCwwLDEsNDEuNzYsMjguMzM3bC4wNDcuNDQ4Wk0zLjgzNCwxLjk0OGgwbS45LDQuNjg4aDAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDM5LjI3MiAxOC4xOTYpIiBmaWxsPSIjN2NiMzQyIi8+CiAgPHBhdGggaWQ9IlBhdGhfNzQ1IiBkYXRhLW5hbWU9IlBhdGggNzQ1IiBkPSJNMTUuMjA2LDMuOTI5LDkuMzcsMTAuNzEyLDE3LjIzLDE2LjksMTQuMjc5LDIwLjY1LDQuNDYxLDEyLjkyNSwyLjUsMTEuMzg0LDQuMTI1LDkuNSwxMS41ODIuODI4WiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMzQuODg1IDExLjU0NikiIGZpbGw9IiM2ODlmMzgiLz4KPC9zdmc+Cg==");
        let pertitle = document.createElement("div");
        pertitle.setAttribute("class", "per-title");
        pertitle.appendChild(document.createTextNode("One more step to go before you start torrenting"));
        let perPargh1 = document.createElement("p");
        perPargh1.setAttribute("class", "p1");
        perPargh1.appendChild(document.createTextNode("This extension can sync results with BitTorrent and/or uTorrent. If you want to activate this feature, please click on the button below, then on the Chrome message to activate the “Messaging Permission”"));
        let perBtn = document.createElement("button");
        perBtn.setAttribute("class", "per-btn");
        perBtn.appendChild(document.createTextNode("Activate Messaging Permission"));
        let perPargh2 = document.createElement("p");
        perPargh2.setAttribute("class", "p2");
        perPargh2.appendChild(document.createTextNode("You can always toggle this option on from the settings menu."));
        let noThanksLink = document.createElement("a");
        noThanksLink.setAttribute("class", "per-link");
        noThanksLink.setAttribute("href", "javascript:void(0);");
        noThanksLink.appendChild(document.createTextNode("No thanks"));

        let overlay = document.createElement('div');
        overlay.setAttribute('class', 'permission-overlay');

        containerPermission.appendChild(perImg);
        containerPermission.appendChild(pertitle);
        containerPermission.appendChild(perPargh1);
        containerPermission.appendChild(perBtn);
        containerPermission.appendChild(perPargh2);
        containerPermission.appendChild(noThanksLink);
        permissionPanel.appendChild(containerPermission);
        wrapper.appendChild(permissionPanel);

        mainContainer.appendChild(overlay);

        perBtn.addEventListener('click', () => {
            chrome.runtime.sendMessage({
                what: 'requestPermissions',
                permissions: ['nativeMessaging']
            }, (result) => {
                if (result.request === true) {
                    // reload page
                    window.location.reload();
                } else {
                    chrome.storage.local.set({ openPanelCount: 3 });
                    window.location.reload();
                }
            });
        });

        noThanksLink.addEventListener('click', () => {
            permissionPanel.remove();
            overlay.remove();
        }); 
    }

    chrome.runtime.sendMessage({
        what: 'containsPermissions',
        permissions: ['nativeMessaging']
    }, (result) => {
        if (result.request === true) {
            nativeMessagingButton.style.display = 'none';
        } else {
            if (browserEnvironment.BrowserFamily != "Edge") {
                chrome.runtime.sendMessage({
                    what: 'requestPermissionBanner'
                }, (result) => {
                    if (result) {
                        if (result.count < 2) {
                            createPermissionBanner();
                        }
                    }
                });
            }
        }
    });

    nativeMessagingButton.addEventListener('click', () => {
        chrome.runtime.sendMessage({
            what: 'requestPermissions',
            permissions: ['nativeMessaging']
        }, (result) => {
            if (result.request === true) {
                // reload page
                window.location.reload();
            } else {
                window.location.reload();
            }
        });
    });

    chrome.storage.local.get({ 'licenseData': null }, (data) => {
        
        if (data.licenseData !== null) {
            hasLicense = data.licenseData.isActive;
            if (data.licenseData.description.toLowerCase().includes('bittorrent')) {
                licenseSpan.innerHTML = 'BitTorrent Web Pro';
                logo.src = chrome.runtime.getURL('img/popup/bittorrent-pro-logo.png');
                settingLogo.src = chrome.runtime.getURL('img/popup/bittorrent-pro-logo.png');
            } else if (data.licenseData.description.toLowerCase().includes("utorrent")) {
                licenseSpan.innerHTML = 'uTorrent Web Pro';
                logo.src = chrome.runtime.getURL('img/popup/utorrent-web-pro-logo.png');
                settingLogo.src = chrome.runtime.getURL('img/popup/utorrent-web-pro-logo.png');
            } else {
                logo.src = chrome.runtime.getURL('img/popup/torrent-pro-logo.png');
                settingLogo.src = chrome.runtime.getURL('img/popup/torrent-pro-logo.png');
            }
        } else {
            logo.src = chrome.runtime.getURL('img/popup/sts-free-logo.png');
            settingLogo.src = chrome.runtime.getURL('img/popup/sts-free-logo.png');
        }

        if (hasLicense === false) {
            upgradeToProBtn.style.display = 'block';
            createPromotionBanner();
        } else {
            settingsBtn.style.display = 'block';
            licenseInput.placeholder = 'License Activated';
            licenseInput.disabled = true;
            licenseButton.disabled = true;
        }
    });

    const createPromotionBanner = () => {
        if (!hasLicense) {
            let upgradeProPanel = document.createElement("div");
            upgradeProPanel.setAttribute("class", "upgradeProPanel");
            let title = document.createElement("div");
            title.setAttribute("class", "upgradeProPanelTitle");
            title.appendChild(document.createTextNode("Try our Pro Versions to unlock:"));

            let upgradeProPanelList = document.createElement("div");
            upgradeProPanelList.setAttribute("class", "upgradeProPanelList");
            let check1 = document.createElement("span");
            let text1 = document.createElement("p");
            let proPanelList1 = document.createElement("div");
            let check2 = document.createElement("span");
            let text2 = document.createElement("p");
            let proPanelList2 = document.createElement("div");
            let check3 = document.createElement("span");
            let text3 = document.createElement("p");
            let proPanelList3 = document.createElement("div");
            let check4 = document.createElement("span");
            let text4 = document.createElement("p");
            let proPanelList4 = document.createElement("div");

            text1.append(check1, document.createTextNode("Faster Results")); 
            text2.append(check2, document.createTextNode("Secure Torrenting"));
            text3.append(check3, document.createTextNode("Unlimited Search Results with detailed torrent info"));
            text4.append(check4, document.createTextNode("1-YR Subscription to CyberGhost VPN (PRO+VPN only)"));
            proPanelList1.append(text1);
            proPanelList2.append(text2);
            proPanelList3.append(text3);
            proPanelList4.append(text4);
            upgradeProPanelList.append(proPanelList1, proPanelList2, proPanelList3, proPanelList4);

            let buyProVpnButton = document.createElement("a");
            buyProVpnButton.setAttribute("class", "upgrade-to-pro-button-2");
            buyProVpnButton.setAttribute("id", "buy-pro-vpn");
            buyProVpnButton.appendChild(document.createTextNode("BUY PRO + VPN"));
            buyProVpnButton.setAttribute("href", "https://www.utorrent.com/webpro-offer/?utm_source=Lavasoft&utm_medium=version_1.0&utm_campaign=Scanner");
            buyProVpnButton.setAttribute("target", "_blank");

            let buyProButton = document.createElement("a");
            buyProButton.setAttribute("class", "upgrade-to-pro-button-2");
            buyProButton.setAttribute("id", "buy-pro");
            buyProButton.appendChild(document.createTextNode("BUY PRO"));
            buyProButton.setAttribute("href", "https://www.utorrent.com/webpro-offer/?utm_source=Lavasoft&utm_medium=version_1.0&utm_campaign=Scanner");
            buyProButton.setAttribute("target", "_blank");

            upgradeProPanel.append(title, upgradeProPanelList, buyProVpnButton, buyProButton);
            mainContainer.appendChild(upgradeProPanel);

            buyProButton.addEventListener("click", () => {
                
                chrome.runtime.sendMessage({
                    what: 'eventType',
                    name: 'UpgradetoProButton',
                    clicked: 'button'
                });
            });

            chrome.storage.local.get({ 'b' : null }, function(data) {
                if (data.b == "bt") {
                    licenseSpan.innerHTML = "BitTorrent Web Pro";
                } else {
                    licenseSpan.innerHTML = "µTorrent Web Pro";
                }
            });

            if (getParameterByName("openSection", window.location.href) == "setting") {
                settingWrapper.style.display = "block";
                wrapper.style.display = "none";
            }
        }
    }

    const sortTorrents = (torrents) => {
        let sortedTorrents = [];

        for (let index in torrents) {
            let website = torrents[index].url || null;
            let torrentData = torrents[index].torrentData || [];
            let torrentLinks = torrents[index].torrentLinks || [];

            for (let i in torrentData) {
                sortedTorrents.push(
                    {
                        website: website, 
                        torrentLinks: torrentLinks[i],
                        torrentData: torrentData[i]
                    }
                );
            }
        }

        
        sortedTorrents.sort((a, b) => parseFloat(b.torrentData.seeders) - parseFloat(a.torrentData.seeders));

        return sortedTorrents
    }

    const appendTorrentToTable = (result) => {
        let data = result || null;
        if (data) {
            let torrent = data.torrentData;
            let torrentLink = (torrent.magnetUri) ? torrent.magnetUri : data.torrentLink;
            let name = torrent?.info?.name || torrent?.infoHash;
            let fileFormatReg = /(?:\.([^.]+))?$/;
            let file = getFile(torrent?.info?.files) || null;
            let fileExt = fileFormatReg.exec(file.name);
            let fileLang = getFileLanguage(name);
            let filePixel = getFilePixel(name);
            let fileSize = formatBytes(file.length) || null;

            // 
            // 
            // 
            // 
            // 
            // 

            // create element here to display the data
            let row = document.createElement('div');
            row.setAttribute('class', 't-row');
            row.setAttribute('data-id', torrent.infoHash);
            let trow = document.createElement('div');
            trow.setAttribute('class', 't-torrent');
            
            if (!hasLicense) {
                if (numTorrents > 5) {
                    row.setAttribute('class', 'display-none');
                }
            }

            let tname = document.createElement('div');
            tname.setAttribute('class', 't-name-text');
            let tlink = document.createElement('a');
            tlink.setAttribute('class', 'torrent-link');
            tlink.setAttribute('target', '_blank');
            tlink.setAttribute('href', torrentLink);
            tlink.addEventListener('click', () => {
                chrome.runtime.sendMessage({
                    what: 'eventType',
                    name: 'torrentType',
                    clicked: 'link'
                });
            });

            let tnameSpan = document.createElement('span');
            tnameSpan.setAttribute('class', 'torrent-title');
            tnameSpan.setAttribute('title', name);
            tnameSpan.appendChild(document.createTextNode(add3Dots(name, 35)));
            let overflow = document.createElement('div');
            overflow.setAttribute('class', 'overflow');
            let tquality = document.createElement('div');
            tquality.setAttribute('class', 't-quality-text');
            tquality.appendChild(document.createTextNode(filePixel));
            let tarrow = document.createElement('div');
            tarrow.setAttribute('class', 't-arrow');
            let tarrowIcon = document.createElement('span');
            tarrowIcon.setAttribute('class', 'arrow-down');
            tarrowIcon.addEventListener('click', (ev) => {
                for (let i = 0; i < ev.path[3].childNodes.length; i++) {
                    if (ev.path[3].childNodes[i].className.indexOf('t-torrent-more') != -1) {
                        ev.path[3].childNodes[i].classList.toggle('show-info');
                    }
                }

                if (ev.target.className == 'arrow-down') {
                    ev.target.className = ev.target.className.replace('arrow-down', 'arrow-up');
                } else {
                    ev.target.className = ev.target.className.replace('arrow-up', 'arrow-down');
                }
            }); 

            let tlangText = document.createElement('div');
            tlangText.setAttribute('class', 't-lang-text');
            tlangText.appendChild(document.createTextNode(fileLang));
            let tstatus = document.createElement('div');
            
            if (torrent.status === 1 || torrent.status == undefined) {
                tstatus.setAttribute('class', 't-status-text t-secure-icon');
            } else {
                tstatus.setAttribute('class', 't-status-text t-insecure-icon');
            }
            
            torrentTableQuality.style.display = 'inline-block';
            if (!hasLicense) {
                torrentTableLang.style.display = 'inline-block';
                torrentTableStatus.style.display = 'none';
                tstatus.style.display = 'none';
            } else {
                torrentTableStatus.style.display = 'inline-block';
                torrentTableLang.style.display = 'none';
                tlangText.style.display = 'none';
            }

            let torrentInfoSection = document.createElement('div');
            torrentInfoSection.setAttribute('class', 't-torrent-more');
            let infoLeft = document.createElement('div');
            infoLeft.setAttribute('class', 't-info-left');
            let infoRight = document.createElement('div');
            infoRight.setAttribute('class', 't-info-right');
            let tsize = document.createElement('span');
            tsize.setAttribute('class', 't-torrent-size');
            tsize.appendChild(document.createTextNode(fileSize));
            let tseeds = document.createElement('span');
            tseeds.setAttribute('class', 't-torrent-seeds');
            let seedsIcon = document.createElement('img');
            seedsIcon.setAttribute('src', chrome.runtime.getURL('img/popup/seeds-icon.svg'));
            let tleeches = document.createElement('span');
            tleeches.setAttribute('class', 't-torrent-leeches');
            let leechesIcon = document.createElement('img');
            leechesIcon.setAttribute('src', chrome.runtime.getURL('img/popup/leech-icon.svg'));
            let lowAvailability = document.createElement('span');
            lowAvailability.setAttribute('class', 't-low-availability');
            lowAvailability.appendChild(document.createTextNode('Low availability'));
            let tfilename = document.createElement('span');
            tfilename.setAttribute('class', 't-torrent-filename');
            tfilename.setAttribute('title', file.name);
            let filenameIcon = document.createElement('img');
            filenameIcon.setAttribute('src', chrome.runtime.getURL('img/popup/torrent-icon.svg'));
            let tpath = document.createElement('span');
            tpath.setAttribute('class', 't-torrent-path');
            tpath.setAttribute('title', (data.website).toString().replace(/^(?:https?:\/\/)?(?:www\.)?/i, ''));
            let pathIcon = document.createElement('img');
            pathIcon.setAttribute('src', chrome.runtime.getURL('img/popup/location-icon.svg'));
            let tbug = document.createElement('span');
            tbug.setAttribute('class', 't-torrent-virus');
            let bugIcon = document.createElement('img');
            bugIcon.setAttribute('src', chrome.runtime.getURL('img/popup/bug-icon.svg'));
            let tlang = document.createElement('span');
            tlang.setAttribute('class', 't-torrent-lang');
            let langIcon = document.createElement('img');
            langIcon.setAttribute('src', chrome.runtime.getURL('img/popup/lang-icon.svg'));
            let sumAvail = 0;
            let numSeeders = 0;
            let numLeechers = 0;
            let virusName = '-';

            if (torrent.seeders && torrent.leechers) {
                numSeeders = torrent.seeders;
                numLeechers = torrent.leechers;
                sumAvail = numSeeders + numLeechers;
            }

            // Append elements
            tarrow.appendChild(tarrowIcon);
            tname.appendChild(tnameSpan);
            tlink.appendChild(tname);
            trow.append(tlink, tstatus, tquality, tlangText, tarrow);
            row.appendChild(trow);
            tseeds.append(seedsIcon, document.createTextNode(numSeeders));
            tleeches.append(leechesIcon, document.createTextNode(numLeechers));
            if (sumAvail <= 5) {
                infoLeft.append(tsize, lowAvailability);
            } else {
                infoLeft.append(tsize, tseeds, tleeches);
            }
            tfilename.append(filenameIcon, document.createTextNode(' ' + add3Dots(file.name, 35)));
            tpath.append(pathIcon, document.createTextNode(' ' + add3Dots((data.website).toString().replace(/^(?:https?:\/\/)?(?:www\.)?/i, ''), 35)));
            tbug.append(bugIcon, document.createTextNode(' ' + add3Dots(virusName, 35)));
            tlang.append(langIcon, document.createTextNode(' ' + fileLang));
            if (!hasLicense) {
                infoRight.append(tfilename, tpath, tbug);
            } else {
                infoRight.append(tfilename, tpath, tbug, tlang);
            }
            torrentInfoSection.append(infoLeft, infoRight);

            if (!hasLicense) {
                if (numTorrents < numTorrentDisplayForFreeUser) {
                    row.appendChild(torrentInfoSection);
                    torrentTableBody.appendChild(row);
                }
            } else {
                checkSection.style.display = "block";
                // maliciousCount.innerHTML = countBadTorrents(torrents.unsafe);
                row.appendChild(torrentInfoSection);
                torrentTableBody.appendChild(row);
            } 

            numTorrents++;
        }

        if (numTorrents > 0) {
            // remove loading elements
            loadingContainer.remove();
            // append torrents count
            torrentNum.innerHTML = numTorrents;

             // send number of torrents to background (badge)
             chrome.runtime.sendMessage({
                what: 'badgeCount',
                count: numTorrents
            });     
        }
    }

    const updateTorrentInTable = (torrentHealths, torrentList) => {
        let data = torrentHealths || [];
        let rows = popup.shadowRoot.querySelectorAll(".t-row");
        let badTorrents = [];

        
        
        
        if (data.length > 0) {
            for (let index = 0; rows.length > index; index++) {
                for (let i in data) {
                    if (rows[index].dataset.id === data[i].infoHash) {
                        // if bad torrent [status=2] found, remove the current row and add to bad torrent array
                        if (data[i]?.status === 2) {
                            badTorrents.push(torrentList[index]);
                            rows[index].remove();
                        }

                        // modify and update table row [status, leechers, seeders, virusName]
                        let leechers = data[i]?.leechers || 0;
                        let seeders = data[i]?.seeders || 0;

                        if (leechers && seeders) {
                            if ((leechers + seeders) > 5) {
                                let tseeds = document.createElement('span');
                                tseeds.setAttribute('class', 't-torrent-seeds');
                                let seedsIcon = document.createElement('img');
                                seedsIcon.setAttribute('src', chrome.runtime.getURL('img/popup/seeds-icon.svg'));
                                let tleeches = document.createElement('span');
                                tleeches.setAttribute('class', 't-torrent-leeches');
                                let leechesIcon = document.createElement('img');
                                leechesIcon.setAttribute('src', chrome.runtime.getURL('img/popup/leech-icon.svg'));
                                tseeds.append(seedsIcon, document.createTextNode(seeders));
                                tleeches.append(leechesIcon, document.createTextNode(leechers));

                                rows[index].children[1].children[0].children[1].remove();
                                rows[index].children[1].children[0].appendChild(tseeds);
                                rows[index].children[1].children[0].appendChild(tleeches);
                            }
                        }
                    }
                }
            }

            // display count for bad torrent based badTorrents array length
            popup.shadowRoot.querySelector(".mal-count").innerHTML = badTorrents.length;
        }
    } 

    chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
        if (request.text == "reloadPage") {
            window.location.reload();
            sendResponse("reloadPage reloaded");
        }

        if (request.text == "getWindowSize") {
            sendResponse({ h: window.innerHeight, w: window.innerWidth });
        }

        if (request.text == "togglePopup") {
            let popup = document.getElementById("torrent-scanner-popup");
            if (popup.style.display === "block") {
                popup.style.display = "none";
                sendResponse({ message: "popupClosed" });
            } else {
                popup.style.display = "block";
                sendResponse({ message: "popupOpened" });
            }
        }
        
        if (request.message == 'torrentData') {
            
            if (request) {
                // Open popup if magnet and torrents found
                popup.style.display = 'block';

                let data = request.data;

                for (let i in data.torrentData) {
                    if (data.torrentData[i].infoHash !== undefined) {
                        let found = torrentArray.some(obj  => obj.infoHash == data.torrentData[i].infoHash);
                        torrentArray.push({ infoHash: data.torrentData[i].infoHash, torrentData: data.torrentData[i], torrentLink: data.torrentLinks[i], website: data.url });
                        // check if torrentArray contains infoHash before append
                        if (found === false) {
                            appendTorrentToTable({ infoHash: data.torrentData[i].infoHash, torrentData: data.torrentData[i], torrentLink: data.torrentLinks[i], website: data.url });
                        }
                        
                    }
                }

                if (request.last) {
                    setTimeout(() => {
                        
                        let trackersObj = mapTorrentTrackers(torrentArray); 
                        
                        socketIoResponse(trackersObj).then((result) => {
                            
                            // merge socket io data with the current data
                            updateTorrentInTable(result, torrentArray);
                            
                            chrome.runtime.sendMessage({
                                what: 'sendListDownloadEvent',
                                url: currentUrl,
                                hostname: (new URL(currentUrl)).hostname,
                                searchQuery: getParameterByName(currentUrl, "q"),
                                queryInput: 'Browser',
                                total: numTorrents,
                                badTorrents: 0
                            });
                        });
                    }, 3000);
                }

                // display query to input
                searchInput.value = request.searchQuery;
            }
            sendResponse("torrentData received");
        }

        return true;
    });
