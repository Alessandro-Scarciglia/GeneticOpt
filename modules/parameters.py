# Data on features
units = {
    "processors": {
        "LEON4": {"power": 5, "weight": 0.5, "processing_power": 500, "cost": 50000},
        "LEON2": {"power": 3, "weight": 0.3, "processing_power": 200, "cost": 30000},
        "MyriadX": {"power": 10, "weight": 0.4, "processing_power": 1000, "cost": 40000},
        "Myriad2": {"power": 7, "weight": 0.35, "processing_power": 700, "cost": 35000},
        "iMX8": {"power": 4, "weight": 0.25, "processing_power": 600, "cost": 25000},
        "Zynq7000": {"power": 8, "weight": 0.45, "processing_power": 800, "cost": 45000},
        "Snapdragon855": {"power": 5, "weight": 0.3, "processing_power": 900, "cost": 50000},
        "JetsonTX2": {"power": 7, "weight": 0.5, "processing_power": 1200, "cost": 60000},
        "RaspberryPi4": {"power": 3, "weight": 0.2, "processing_power": 400, "cost": 20000},
        "RK3399": {"power": 6, "weight": 0.4, "processing_power": 650, "cost": 30000}
    },
    "coprocessors": {
        "VPU": {"power": 2, "weight": 0.1, "processing_power": 250, "cost": 15000},
        "DSP": {"power": 3, "weight": 0.2, "processing_power": 300, "cost": 20000},
        "GPU": {"power": 5, "weight": 0.3, "processing_power": 500, "cost": 25000},
        "FPGA": {"power": 4, "weight": 0.25, "processing_power": 450, "cost": 30000},
        "NNP": {"power": 3, "weight": 0.15, "processing_power": 400, "cost": 20000}
    },
    "inspection_cameras": {
        "CamA": {"power": 2, "weight": 0.2, "fps": 30, "cost": 10000},
        "CamB": {"power": 1.5, "weight": 0.15, "fps": 60, "cost": 12000},
        "CamC": {"power": 2.5, "weight": 0.25, "fps": 45, "cost": 15000}
    },
    "multispectral_cameras": {
        "MultiCamA": {"power": 3, "weight": 0.3, "fps": 20, "cost": 20000},
        "MultiCamB": {"power": 2.5, "weight": 0.25, "fps": 25, "cost": 25000},
        "MultiCamC": {"power": 4, "weight": 0.35, "fps": 30, "cost": 30000}
    }
}