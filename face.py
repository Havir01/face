import json
import facebook
def main():
    token = {"EAACB5CFr39sBAKVr1UZAUlzaZCyjhqIa0zQbpeqzru6G5QJ5Q1epGEb9SAoqrrHhxytNZC2zmWZAoYHHykCL70hoECecY8kjJTElBNwsYs2ZAE59TLAUoT78Sd0xZBFWjpNCEE7t2Tn7mGZBrFky1FvTRFYpFZAcU6UOyPmVfrSyIyox6DuXWidsjPjGPVlgS3gZD"}
    graph = facebook.GraphAPI(token)

    field = ['id,name,email,location']

    #profile = graph.get_object('me',fields = field)
    places = graph.search(type='place',
                      center='10.90726571,-74.7835359',
                      fields='name,location')
    for place in places['data']:
        print(json.dumps('%s %s' % str((place['name'].encode(),place['location'].get('zip'))),indent=4))                  

    #print(json.dumps(profile,indent=4))

if __name__ == "__main__":
    main()
