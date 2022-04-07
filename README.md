# img2address
API that reads an address from an image.

## Workflow
1. Send image to Paigo-OCR: https://collaboration.bertelsmann.de/main/solutions/paigo-ocr-api/product-information
2. Parse address token from text
3. Send address token to Easy Address Validation: https://collaboration.bertelsmann.de/main/solutions/az-direct-address-verification-api/product-information
