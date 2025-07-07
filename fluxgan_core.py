import torch
import torch.nn as nn
import numpy as np

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.main = nn.Sequential(
            nn.Linear(2, 16),
            nn.LeakyReLU(0.2),
            nn.Linear(16, 16),
            nn.LeakyReLU(0.2),
            nn.Linear(16, 2)
        )

    def forward(self, x):
        return self.main(x)

def sample_noise(num_samples, dim):
    return torch.Tensor(np.random.uniform(-1., 1., size=[num_samples, dim]))

def load_model(checkpoint_path):
    model = Generator().to(device)
    checkpoint = torch.load(checkpoint_path, map_location=device)

    if "generator_state_dict" in checkpoint:
        state_dict = checkpoint["generator_state_dict"]
    elif "model_state_dict" in checkpoint:
        state_dict = checkpoint["model_state_dict"]
    else:
        state_dict = checkpoint  # assume raw

    model.load_state_dict(state_dict)
    model.eval()
    return model

def predict_flux(generator, target_enrichment, tolerance=2.5, num_samples=10000):
    generator.to(device)
    with torch.no_grad():
        noise = sample_noise(num_samples, 2).to(device)
        outputs = generator(noise).cpu().numpy()
        enrichments = outputs[:, 0]
        fluxes = outputs[:, 1]

        print(f"Generated enrichment range: {enrichments.min():.2f} to {enrichments.max():.2f}")
        
        mask = (enrichments >= target_enrichment - tolerance) & (enrichments <= target_enrichment + tolerance)
        matched_fluxes = fluxes[mask]
        
        if len(matched_fluxes) > 0:
            return float(np.mean(matched_fluxes))
        else:
            return 0.0
