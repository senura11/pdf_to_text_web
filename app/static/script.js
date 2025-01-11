// static/script.js

function copyToClipboard() {
    const textOutput = document.getElementById('text-output');
    const tempTextArea = document.createElement('textarea');
    tempTextArea.value = textOutput.textContent;
    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    tempTextArea.setSelectionRange(0, 99999);
    document.execCommand('copy');
    document.body.removeChild(tempTextArea);
    alert('Text copied to clipboard!');
    const copyButton = document.getElementById('copy-button');
    copyButton.textContent = 'Copied!';
    setTimeout(() => {
        copyButton.textContent = 'Copy to Clipboard';
    }, 2000);
}