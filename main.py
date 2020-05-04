import json
import csv


def main():
    with open('Geothermal/api.txt') as json_file:
        with open('Geothermal/data.csv',"w") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            data = json.load(json_file)
            submission = data["result"]
            print (len(submission))
            for s in submission:
                submission_name = s["submissionName"]
                api_id = s["_id"]["$id"]
                created = s["created"]
                status = s["status"]
                url = "https://gdr.openei.org/submissions/"+str(s["xdrId"])
                keywords = s["keywords"]
                resources = s["resources"]
                for r in resources:
                    resource_name = r["name"]
                    resource_type = r["resourceType"]
                    if 'coordinates' in r:
                        resource_coordinates = r["coordinates"]
                        if (resource_coordinates):
                            lat = r["coordinates"][0]
                            lng = r["coordinates"][1] 
                            writer.writerow([submission_name,api_id,created,status,url,keywords,resource_name,resource_type,lat,lng])

                            # print (resource_coordinates)


main()