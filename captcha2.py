# from twocaptcha import TwoCaptcha

# key='053f65b8227203daee91903852406ca5'
# url=r'E:\\DJANGO\\irctc_autoomation_app\\recapchabypass\\logo.png'
# solver=TwoCaptcha(key)
# result=solver.normal(url)
# print(result['code'])

import requests
import base64


def solve():
	with open('logo2.png', "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read()).decode('ascii')
		
		url = 'https://api.apitruecaptcha.org/one/gettext'

		data = { 
			'userid':'sarbjitdeol72@gmail.com', 
			'apikey':'hAWX2MbYjpViHGSVhYPX',  
			'data':encoded_string,
			'mode':'human',
			
		}
		response = requests.post(url = url, json = data)
		data = response.json()
		captcha=data
		print(captcha)

solve()
