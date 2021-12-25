from PIL import Image


class normalize():
    miniR = ''
    maxiR = ''
    minoR = ''
    maxoR = ''
    miniG = ''
    maxiG = ''
    minoG = ''
    maxoG = ''
    miniB = ''
    maxiB = ''
    minoB = ''
    maxoB = ''

    @staticmethod
    def iniciajlizujNorm():
        img = Image.open("static/img/magla.jpg")
        img.save('static/img/maglaNormalized.jpg')

    @staticmethod
    def setuj(inpMinR, inpMaxR, outMinR, outMaxR, inpMinG, inpMaxG, outMinG, outMaxG, inpMinB, inpMaxB, outMinB, outMaxB):
        normalize.miniR = int(inpMinR)
        normalize.maxiR = int(inpMaxR)
        normalize.minoR = int(outMinR)
        normalize.maxoR = int(outMaxR)
        normalize.miniG = int(inpMinG)
        normalize.maxiG = int(inpMaxG)
        normalize.minoG = int(outMinG)
        normalize.maxoG = int(outMaxG)
        normalize.miniB = int(inpMinB)
        normalize.maxiB = int(inpMaxB)
        normalize.minoB = int(outMinB)
        normalize.maxoB = int(outMaxB)

    @staticmethod
    def normalizeRed(intensity):
        Pi = intensity
        Po = (Pi - normalize.miniR) * (((normalize.maxoR - normalize.minoR) / (normalize.maxiR - normalize.miniR)) + normalize.minoR)
        return Po

    @staticmethod
    def normalizeGreen(intensity):
        Pi = intensity
        Po = (Pi - normalize.miniG) * (((normalize.maxoG - normalize.minoG) / (normalize.maxiG - normalize.miniG)) + normalize.minoG)
        return Po

    @staticmethod
    def normalizeBlue(intensity):
        Pi = intensity
        Po = (Pi - normalize.miniB) * (((normalize.maxoB - normalize.minoB) / (normalize.maxiB - normalize.miniB)) + normalize.minoB)
        return Po

    @staticmethod
    def norm_kontr():
        image = Image.open("static/img/magla.jpg")
        multiBands = image.split()
        normalized_R = multiBands[0].point(normalize.normalizeRed)
        normalized_G = multiBands[1].point(normalize.normalizeGreen)
        normalized_B = multiBands[2].point(normalize.normalizeBlue)
        normalizedImage = Image.merge("RGB", (normalized_R, normalized_G, normalized_B))
        normalizedImage.save('static/img/maglaNormalized.jpg')
