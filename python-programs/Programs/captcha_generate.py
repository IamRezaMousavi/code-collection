# @Author: @IamRezaMousavi
# @Date:   2022-04-09 14:56:42
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-04-09 15:16:16


def main():
    from random import choices
    from string import ascii_letters, digits

    from captcha.image import ImageCaptcha

    pool = ascii_letters + digits
    output = choices(pool, k=7)

    image = ImageCaptcha(width=300, height=200)
    image.write(''.join(output), 'captcha.png')


if __name__ == '__main__':
    main()
