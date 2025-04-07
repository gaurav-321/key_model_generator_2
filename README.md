# key_model_generator_2

## Description

key_model_generator_2 is a Python program designed to process images, detect valid contours, and save them as OBJ files. This tool is particularly useful for tasks involving 3D modeling from 2D images, such as extracting features from photographs for CAD applications.

## Features
- **Image Processing:** Utilizes OpenCV (cv2) for image processing tasks.
- **Contour Detection:** Automatically detects valid contours in the input image.
- **OBJ File Generation:** Saves detected contours as OBJ files for easy integration into 3D modeling software.
- **Visualization:** Displays the original image with detected contour points labeled.

## Installation

To install and run key_model_generator_2, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/gag3301v/key_model_generator_2.git
   cd key_model_generator_2
   ```

2. **Install Dependencies:**
   The project requires `cv2` and `numpy`. Install them using pip:
   ```bash
   pip install opencv-python numpy
   ```

## Usage

Here’s how you can use the program:

```python
# Import necessary libraries
import cv2
import numpy as np

# Function to create an OBJ file from vertices
def create_obj(vtx):
    with open('output.obj', 'w') as f:
        for v in vtx:
            f.write(f'v {v[0]} {v[1]} 0\n')

# Main processing function
def process_image(image_path):
    # Load image
    img = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to detect edges
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw detected contours on the image
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    
    # Save the image with contours
    cv2.imwrite('output_image.jpg', img)
    
    # Extract vertices from contours and create OBJ file
    vtx = []
    for contour in contours:
        for point in contour:
            vtx.append(point[0])
    create_obj(vtx)

# Example usage
process_image('input_image.jpg')
```

## Configuration

This script does not require any specific configuration settings. Ensure that the input image is correctly specified in the `process_image` function call.

## Tests

No automated tests are provided with this script, but you can manually test it by running:

```bash
python main.py
```

Ensure your input image (`input_image.jpg`) is correctly formatted and contains contours for accurate results.

## Project Structure

- **main.py:** Contains the main processing logic.
- **output.obj:** Output OBJ file containing detected contour points.
- **output_image.jpg:** Image with detected contour points labeled.

## Contributing

Contributions are welcome! If you have any ideas, bug fixes, or improvements, please fork this repository and submit a pull request. Ensure your contributions follow the code style and guidelines of the project.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/gag3301v/key_model_generator_2/blob/main/LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance! 🚀