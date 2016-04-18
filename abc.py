import urllib2
import json 
import csv
import sys

def main():

    DS_type = sys.argv[1]  #To select which API to Hit as per Building
    page_type = sys.argv[2] # To select CSV operation or input


    if page_type == "CSV":
        listoflists = []
        values = str(sys.argv[3])
        header=  str(sys.argv[4])
        abc = []
        abc.append(values.split(','))

        #print(abc)

        data =  {

            "Inputs": {

                    "Input1":
                    {
                        "ColumnNames" : header.split(','),
                        "Values": abc #values.split(',')
                    },        },
                "GlobalParameters": {
        }
            }

        body = str.encode(json.dumps(data))


        if DS_type == "school":
                url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/13bf2e27aa51418a953ddeaf8ec5bfd5/execute?api-version=2.0&details=true'
                api_key = 'Ix6qkPiMr/rIeBSswcAcIK+p3r2QQhMUqA+EmM1nx8C/rOJlUNhYWf1S/3UqUGRx/4lPCc8uC60u3ZeRI0nXbg=='
        elif  DS_type == "BFD":
                url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/ee77034b2d0947f9a675dd11d3aa867e/execute?api-version=2.0&details=true'
                api_key = 'ddMZyeiL/6a14Zlh2BlOfUkkf76A70/0DgtGuWVuXBy9RLploLlDAuAGe5PIP7cLmqcvRC805h7CjxV2ysijZw=='
        elif  DS_type == "BPD":
                url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/13bf2e27aa51418a953ddeaf8ec5bfd5/execute?api-version=2.0&details=true'
                api_key = 'Ix6qkPiMr/rIeBSswcAcIK+p3r2QQhMUqA+EmM1nx8C/rOJlUNhYWf1S/3UqUGRx/4lPCc8uC60u3ZeRI0nXbg=='
        elif  DS_type == "PM":
                url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/25e8f06d5e7048bfa64f92cdb249c274/execute?api-version=2.0&details=true'
                api_key = 'fy4lM67b2VzYJzELzVqqG6zxoodR1OFfi60GbTRabIHaBZfRAJrO1OHhehHKfc8n/TyJnmLGKXQ2JenfPMQUJg=='
        elif  DS_type == "PL":
                url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/13bf2e27aa51418a953ddeaf8ec5bfd5/execute?api-version=2.0&details=true'
                api_key = 'Ix6qkPiMr/rIeBSswcAcIK+p3r2QQhMUqA+EmM1nx8C/rOJlUNhYWf1S/3UqUGRx/4lPCc8uC60u3ZeRI0nXbg=='


        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib2.Request(url, body, headers) 

        try:
            response = urllib2.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

            result = response.read()
            print(result)
        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))  
        #return json.loads(error.read())
    else:
        header = sys.argv[3]
        kopi = str(sys.argv[4])
        abc = []
        abc.append(kopi.split(','))
        header = header.split(',')
      
        #print(abc)

        data =  {

            "Inputs": {

                    "Input1":
                    {
                        "ColumnNames" : header,
                        "Values": abc #values.split(',')
                    },        },
                "GlobalParameters": {
        }
            }


        body = str.encode(json.dumps(data))


        if DS_type == "school":
                url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/13bf2e27aa51418a953ddeaf8ec5bfd5/execute?api-version=2.0&details=true'
                api_key = 'Ix6qkPiMr/rIeBSswcAcIK+p3r2QQhMUqA+EmM1nx8C/rOJlUNhYWf1S/3UqUGRx/4lPCc8uC60u3ZeRI0nXbg=='
        elif  DS_type == "BFD":
                url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/ee77034b2d0947f9a675dd11d3aa867e/execute?api-version=2.0&details=true'
                api_key = 'ddMZyeiL/6a14Zlh2BlOfUkkf76A70/0DgtGuWVuXBy9RLploLlDAuAGe5PIP7cLmqcvRC805h7CjxV2ysijZw=='
        elif  DS_type == "BPD":
                url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/13bf2e27aa51418a953ddeaf8ec5bfd5/execute?api-version=2.0&details=true'
                api_key = 'Ix6qkPiMr/rIeBSswcAcIK+p3r2QQhMUqA+EmM1nx8C/rOJlUNhYWf1S/3UqUGRx/4lPCc8uC60u3ZeRI0nXbg=='
        elif  DS_type == "PM":
                url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/25e8f06d5e7048bfa64f92cdb249c274/execute?api-version=2.0&details=true'
                api_key = 'fy4lM67b2VzYJzELzVqqG6zxoodR1OFfi60GbTRabIHaBZfRAJrO1OHhehHKfc8n/TyJnmLGKXQ2JenfPMQUJg=='
        elif  DS_type == "PL":
                url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/13bf2e27aa51418a953ddeaf8ec5bfd5/execute?api-version=2.0&details=true'
                api_key = 'Ix6qkPiMr/rIeBSswcAcIK+p3r2QQhMUqA+EmM1nx8C/rOJlUNhYWf1S/3UqUGRx/4lPCc8uC60u3ZeRI0nXbg=='


        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib2.Request(url, body, headers) 

        try:
            response = urllib2.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

            result = response.read()
            print(result)
        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read())) 
        

if __name__ == "__main__":
    main()
    #print('MAIN KE ANDAR')
    
