import os
from PIL import Image
import logging

ORIGINALS = "original"
OPTIMIZED = "static/images/optimized"

def optimize_all(logger: logging.Logger):
    for file in os.listdir(ORIGINALS):
        base_name = os.path.splitext(file)[0]
        input = os.path.join(ORIGINALS, file)
        output = os.path.join(OPTIMIZED, f"{base_name}.webp")

        if os.path.exists(output):
            logger.info(f" skipping {file}\t\t(optimized ver. exists)")
            continue
        else:
            logger.info(f" optimizing {file} ...")

        try:
            with Image.open(input) as img:
                if img.mode not in ('RGB', 'RGBA'):
                    img = img.convert('RGBA')

                img.save(output, 'WEBP', quality=5)
        except Exception as e:
            logger.error(f" failed to optimize {file}")
            logger.debug(e)

    logger.info(" done with optimizations!")
