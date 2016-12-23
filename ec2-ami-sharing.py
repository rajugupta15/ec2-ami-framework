#!/usr/bin/python
import json
import sys
import datetime
data_file = open('amiDetails.json', 'r')
data = json.load(data_file)
imagelist = (list(data.keys()))

class amiJson():


    def amiJsonStack(self, aminame):
        if aminame in imagelist:
            amistack = (data[aminame])
            return amistack
        else:
            return(aminame + ' ' + 'is not Found in json')
            sys.exit()

    def amiReleDateFromJson(self, aminame):
        if aminame in imagelist:
            amistack = self.amiJsonStack(aminame)
            amireleasedate = amistack['AMI_RELEASE_DATE']
            return amireleasedate
        else:
            return(aminame + ' ' + 'is not Found in json')
            sys.exit()


    def amiIdFromJson(self, aminame):
        if aminame in imagelist:
            amistack = self.amiJsonStack(aminame)
            amiid = amistack['AMI_ID']
            return amiid
        else:
            return(aminame + ' ' + 'is not Found in json')
            sys.exit()

    def amiReleVersionFromJson(self, aminame):
        if aminame in imagelist:
            amistack = self.amiJsonStack(aminame)
            amireleaseversion = amistack['AMI_RELEASE_VERSION']
            return amireleaseversion
        else:
            return(aminame + ' ' + 'is not Found in json')
            sys.exit()


    def amiSharedDate(self):
        dateofsharing = datetime.datetime.now().strftime("%Y-%m-%d")
        return dateofsharing


def main():
        jsonValue = amiJson()
        imageid= jsonValue.amiIdFromJson('WME-3.2.2')
        releaseDate = jsonValue.amiReleDateFromJson('WME-3.2.2')
        amiversion = jsonValue.amiReleVersionFromJson('WME-3.2.2')
        shareddate = jsonValue.amiSharedDate()
        print(releaseDate)
        print(imageid)
        print(amiversion)
        print(shareddate)
if __name__ == "__main__":
    main()
