# © 2018 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import base64
from PIL import Image
from io import BytesIO
from odoo import tools


def process_image(b64data, size):
    if isinstance(b64data, str):
        b64data = bytes(b64data, 'utf-8')

    image = Image.open(BytesIO(base64.b64decode(b64data)))

    asked_w, asked_h = size
    if asked_w is None:
        asked_w = int(image.size[0] * (float(asked_h) / image.size[1]))
    if asked_h is None:
        asked_h = int(image.size[1] * (float(asked_w) / image.size[0]))
    size = asked_w, asked_h

    # check image size: do not create a thumbnail if avoiding smaller images
    if image.size[0] <= size[0] and image.size[1] <= size[1]:
        return b64data

    image = tools.image_resize_and_sharpen(image, size)
    image = tools.image_save_for_web(image, format='JPEG')

    return base64.b64encode(image)
