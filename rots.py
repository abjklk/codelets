import requests
import json

form = {'sectionId': '25dc48a8-eb97-46de-9e5f-6e24d6aadad0',
		'questionId': 'db69878e-2dce-49fd-8dd2-9874fd662099',
		'resultId': '68b092ab-95c6-4c0f-8f9b-49f01039e5bf',
		'recaptchaToken': '03AGdBq27KTdphF7Wx3bJ3EZch2xo9o1JjQwCDtY6igrDz8yKctLGAgXRBXCEMi7rWE06freu0jFOSEqZCbds72yNj1gvjlXUFj2elYgr8CnnuZpnagbV8xh_5n27XYvkODFNQI0ny6ReLk94SzeUIslVMbXmhYxi8LCYLdYr8MeJcIe2pRqla_gEBAml_UHWZADbU8C08rPuQpEnAgVS1jqK8c1k_os-KljPozxSmJLfyEsUbv_ieYr0cD3MGx9jhDLvXm_Tylb9tRXp1lGnAtNaT5b6MgJpH30qNlgB8JAGEp-qw1oxID-MKn0JDDPbcNFk9f7foqibi_ExKSy6dtJ72f-AtDi-H43b0k-BfZn62Li0TC3ZogrMNit_ZpSGUhQ66AB9_9HCwJuXKXyxd7CzoWU4a32sbTRVCugSRMyK4ePLj2QUb5zNHdBDt8XEtHNchUiSM9OxioA93mqs9Jp3lrsQTB2jUjg'}

for i in range(1000):
	a = requests.post('https://voting.playbuzz.com/poll/',data=form)
	# rots = int(dict(json.loads(a.content)['results'])['973abd80-01aa-4563-bbf6-a58c827e402d'])
	# dkr = int(dict(json.loads(a.content)['results'])['536abfed-fe29-41c7-bafa-10de723ea38a'])
	# print(rots,dkr)
	# print(rots-dkr)
	print(a.content)
