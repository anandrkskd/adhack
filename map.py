#!/usr/bin/env python3
# importing googlemaps module
import googlemaps
import webbrowser

# Printing the result
fromm="jaipur"
to='chittaranjan'

#program to find distance between two cities
def dist(fromm,to):
    #api key to connect to google map 
    gmaps = googlemaps.Client(key='AIzaSyCftOPhqDZCDbgbUvHXQMDhMO_aGsC9we8')
    my_dist = gmaps.distance_matrix(fromm,to)['rows'][0]['elements'][0]      #fetching the data of distance
    print("\n\n"+str(my_dist['distance']["text"]))


#program to find time required between to cities
def timed(fromm,to):
    #api key to connect to google map 
    gmaps = googlemaps.Client(key='AIzaSyCftOPhqDZCDbgbUvHXQMDhMO_aGsC9we8')
    my_dist = gmaps.distance_matrix(fromm,to)['rows'][0]['elements'][0]             #fetching the data of time required to reach between to cities
    print("\n\n"+str(my_dist["duration"]["text"]))


#to search for some certain near by place
def search(place):
    #api key to connect to google map 
    gmaps = googlemaps.Client(key='AIzaSyCftOPhqDZCDbgbUvHXQMDhMO_aGsC9we8')
    search="https://www.google.co.in/maps/place/"                   #google map url for searching certain location
    query=place                                                     #place to be searched for 
    webbrowser.open(search+query)



#search(fromm)
#dist(fromm,to)
#timed(fromm, to)



if __name__=="__main__":
    dist(fromm,to)
    timed(fromm,to)
    search(fromm)
