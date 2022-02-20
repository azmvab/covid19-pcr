import os

import qrcode
from django.conf import settings
from django.http import FileResponse
from django.views import generic
from PIL import Image, ImageDraw, ImageFont
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import VerticalGradiantColorMask
from qrcode.image.styles.moduledrawers import CircleModuleDrawer

from .models import Person


class PeopleDetailView(generic.DetailView):
    slug_field = "guid"
    template_name = 'index.html'
    queryset = Person.objects.all()


class PeopleImageView(generic.DetailView):
    slug_field = "guid"
    template_name = 'index.html'
    queryset = Person.objects.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        img = Image.open(os.path.join(settings.MEDIA_ROOT, "layer.jpg"), mode='r')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(os.path.join(settings.MEDIA_ROOT, "font.ttf"), size=46)
        draw.text((480, 400), self.object.name, (0,0,0), font=font)
        draw.text((480, 505), self.object.identification_id, (0,0,0), font=font)
        draw.text((480, 610), self.object.birthday.strftime("%d-%m-%Y") , (0,0,0), font=font)
        draw.text((480, 715), self.object.nationality, (0,0,0), font=font)
        draw.text((480, 820), self.object.mobile, (0,0,0), font=font)
        draw.text((1670, 505), self.object.collection_time.strftime("%Y-%m-%d          %H:%M:%S"), (0,0,0), font=font)
        draw.text((1670, 610), self.object.result_time.strftime("%Y-%m-%d          %H:%M:%S"), (0,0,0), font=font)
        draw.text((1670, 715), self.object.report_no, (0,0,0), font=font)
        draw.text((1670, 820), self.object.hesn_no, (0,0,0), font=font)
        url = request.build_absolute_uri(self.object.get_absolute_url())
        qr = qrcode.QRCode(version=7, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=2)
        qr.add_data(url)
        logo = Image.open(os.path.join(settings.MEDIA_ROOT, "logo.png"), mode='r')
        logo.convert("RGBA")
        logo = logo.resize((120, 180), Image.ANTIALIAS)
        qr_img = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer(), color_mask=VerticalGradiantColorMask(back_color=(255, 255, 255), top_color=(190, 58, 56), bottom_color=(19, 8, 14)))
        qr_img.paste(logo, (210, 170))
        img.paste(qr_img, (280, 2860))
        img.save(os.path.join(settings.MEDIA_ROOT, f"images/layer-{self.object.guid}.jpg"))
        
        return FileResponse(open(os.path.join(settings.MEDIA_ROOT, f"images/layer-{self.object.guid}.jpg"), 'rb'), content_type='image/jpeg')
