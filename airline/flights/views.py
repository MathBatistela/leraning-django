from django.shortcuts import render
from flights.models import Flight, Passenger
from django.http import HttpResponseRedirect, HttpResponseBadRequest, Http404
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from flights.serializers import FlightModelSerializer

@api_view(['GET'])
def index(request):
    # renderer_classes = (TemplateHTMLRenderer,JSONRenderer)
    flightsobjcts = Flight.objects.all()

    print("-------------------------------------------------------")
    print(request.accepted_renderer.format)
    if request.accepted_renderer.format == 'json':
        serializer = FlightModelSerializer(flightsobjcts, many=True)
        data = serializer.data
        return Response(data)


    data = {'flights': flightsobjcts}
    return Response(data, template_name='flights/index.html')
    
    
def flight(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight not found.")
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })
    
def book(request, flight_id):
    if request.method == "POST":
        try:
            passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
            flight = Flight.objects.get(pk=flight_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no flight chosen")
        except Flight.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: flight does not exist")
        except Passenger.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: passenger does not exist")
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
    
    