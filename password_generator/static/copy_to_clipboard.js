function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then( () => {
        alert("Copied To Clipboard "+ text);
    }).catch(err => {
        console.error("Fail To copy: ", err)
    });
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("copyButton").addEventListener("click", function() {
        let textToCopy = this.getAttribute("data-text");
        copyToClipboard(textToCopy);
    });
});