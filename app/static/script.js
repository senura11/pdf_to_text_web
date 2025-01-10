function copyToClipboard() {
    // Create a temporary textarea element
    const textOutput = document.getElementById('text-output');
    const tempTextArea = document.createElement('textarea');
    
    // Set the value of the textarea to the text content
    tempTextArea.value = textOutput.textContent;
    
    // Append the textarea to the document body
    document.body.appendChild(tempTextArea);
    
    // Select the text inside the textarea
    tempTextArea.select();
    tempTextArea.setSelectionRange(0, 99999); // For mobile devices
    
    // Copy the selected text to the clipboard
    document.execCommand('copy');
    
    // Remove the temporary textarea from the document
    document.body.removeChild(tempTextArea);
    
    // Optional: Notify the user that the text has been copied
    alert('Text copied to clipboard!');
    
    // Optional: Change the button text temporarily
    const copyButton = document.getElementById('copy-button');
    copyButton.textContent = 'Copied!';
    setTimeout(() => {
        copyButton.textContent = 'Copy to Clipboard';
    }, 2000); // Reset the button text after 2 seconds
}
