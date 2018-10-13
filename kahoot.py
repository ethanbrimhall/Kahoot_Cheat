import requests
import json
import credentials

def get_kahoot(kahootid, email, passwd):

    authparams = {'username':email,'password':passwd,'grant_type':'password'}

    print('AUTHENTICATING username and password...')

    data = requests.post('https://create.kahoot.it/rest/authenticate', data=json.dumps(authparams).encode(),headers={'content-type':'application/json'}).json()

    if 'error' in data:
        print('Authenication Failed!\n')
        exit()


    response = requests.get('https://create.kahoot.it/rest/kahoots/{}'.format(kahootid), headers={'content-type' : 'application/json','authorization' : data['access_token']}).json()

    questions = []

    if 'error' in response:
        print("No Kahoot Found!")
        exit()
    else:
        print("FOUND Kahoot titled: '" + response["title"] + "'")

        for i in range(0, len(response["questions"])):
            currentQuestion = {"question": "", "answer": ""}

            currentQuestion["question"] = response["questions"][i]["question"]

            for j in range(0, len(response["questions"][i]["choices"])):
                if response["questions"][i]["choices"][j]["correct"] == True:
                    currentQuestion["answer"] = response["questions"][i]["choices"][j]["answer"]

            questions.append(currentQuestion)

        return questions


kahootid = input("Enter the quiz id from host URL: ")

questions = get_kahoot(kahootid, credentials.email, credentials.password)

print("\nAll Questions: " + str(questions))





