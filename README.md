# FluxGAN-Sim

FluxGAN-Sim is a simulation and modeling toolkit for nuclear reactor flux profiles using Generative Adversarial Networks (GANs). It provides tools for training, evaluating, and visualizing flux distributions for various reactor types.

## Features
- Pre-trained GAN models for multiple reactor types (BWR, FBR, HTGR, LWR, PHWR, PWR)
- Easy-to-use simulation interface
- Visualization of generated flux profiles
- Extensible for research and educational purposes

## Installation
Clone the repository:
```bash
git clone https://github.com/kavyawadhwa134/fluxgan-sim.git
cd fluxgan-sim
```
Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the main application:
```bash
python app.py
```

## Project Structure
- `app.py`: Main application entry point
- `fluxgan_core.py`: Core GAN logic
- `fluxgan_model/`: Pre-trained model files for each reactor type
- `checkpoints/`: Model checkpoints
- `templates/`: Web interface templates

## Author

**Kavya Wadhwa**  
[GitHub](https://github.com/kavyawadhwa134) | [LinkedIn](https://www.linkedin.com/in/kavyawadhwa134)  
website : www.kavyawadhwa.info  
email : kavyavadhwa@gmail.com

Nuclear engineering enthusiast, passionate about AI for science and open-source collaboration.

---

A working demo of this tool is available at: [https://fluxgan-sim.onrender.com](https://fluxgan-sim.onrender.com)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
