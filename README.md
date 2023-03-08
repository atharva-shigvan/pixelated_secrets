# Pixelated Secrets
Pixelated Secrets is an Image and Video Steganography GUI program made in python programming language. Steganography is an art of embedding secret messages into images or videos such that no one can recognise it except the intended recipient. The process includes taking input file which can be a picture or video in our case, then embedding the message using few calculations such that the original file isn't changed visually. Sizes and Hash values of original file and message embedded file will be different. Steganography was used for secret communications especially for military purposes. Pixelated secrets tries to imitate that in an easier way. Now a days, steganography is used for malicious purpose such as hiding trojans. Author of this repository doesn't suggest the use of this repository or any part of the code for malicious purposes. User will be solely reponsible for his/her actions or consequences caused by using the code for harmful purposes.
### Usage:
- Clone the repository to your local machine using git.
> git clone https://github.com/atharva-shigvan/pixelated_secrets

- Make the program executable
> chmod +777 pixelated_secrets.py

- Make sure you have required libraries of python
> pip install -r requirements.txt

- Execute the program
> python3 pixelated_secrets.py

- Select the option whether you want to embed message in image or video. (You can select demo image provided)
- Enter the secret message in text box
- Save the image file in your desired folder. The image will be saved with ```.png``` extension.

If it gave you the expected output don't forget to give me a star ;)
