from db import execute_query, format_records

from flask import Flask

from webargs import fields
from webargs.flaskparser import use_kwargs


app = Flask(__name__)


@app.route("/")
def greating():
    return "<p>HOMEWORK 5</p>"


@app.route("/unique_names")
def get_unique_names():
    query = "select DISTINCT FirstName FROM customers"
    records = execute_query(query)
    return str(len(records))


@app.route("/len_tracks")
def get_len_tracks():
    query = "select * from tracks"
    records = execute_query(query)
    return str(len(records))


@app.route("/cities_countries")
@use_kwargs({
    "city": fields.Str(
        required=False
    ),
    "country": fields.Str(
        required=False
    )},
    location="query"
)
def get_cities(city=None, country=None):
    query = "select City, Country from customers"
    where_filter = {}
    params = []
    if city:
        where_filter['City'] = city
    if country:
        where_filter['Country'] = country

    if where_filter:
        query += ' WHERE ' + ' AND '.join(f'{k}=?' for k, v in where_filter.items())
    params = [v for k, v in where_filter.items()]
    records = execute_query(query, params)
    return format_records(records)


@app.route("/sales")
def get_sales():

    query = "select UnitPrice, Quantity from invoice_items"
    records = execute_query(query)
    summ = 0
    for k, v in records:
        summ += k * v
    return str(summ)


@app.route("/genres_durations")
def get_genre_durations():
    query = "SELECT tracks.MediaTypeId, tracks.Milliseconds/(1000) from tracks GROUP by tracks.MediaTypeId"
    records = execute_query(query)
    return str(records)


@app.route("/greatest_hits")
@use_kwargs({
    "count": fields.Str(
        required=False
     )},
    location="query"
    )
def get_greatest_hits(count=None):
    query = "SELECT TrackId, Quantity*UnitPrice FROM invoice_items ORDER by Quantity*UnitPrice"
    if count:
        query += f' limit {count}'
    records = execute_query(query)
    return str(records)


@app.route("/greatest_artists")
@use_kwargs({
    "count": fields.Str(
        required=False
     )},
    location="query"
    )
def get_greatest_artists(count=None):
    query = """SELECT artists.ArtistId, invoice_items.Quantity * invoice_items.UnitPrice
                from artists
                JOIN albums
                on artists.ArtistId = albums.ArtistId
                JOIN tracks
                on albums.AlbumId = tracks.AlbumId
                JOIN invoice_items
                on tracks.TrackId = invoice_items.TrackId
                GROUP by artists.ArtistId
                ORDER by invoice_items.Quantity * invoice_items.UnitPrice"""
    if count:
        query += f' limit {count}'
    records = execute_query(query)
    return str(records)


@app.route("/stats_by_city")
@use_kwargs({
    "count": fields.Str(
        required=False
    ),
    "genre": fields.Str(
        required=False
     )},
    location="query"
    )
def get_stats_by_city(count=None, genre=None):
    if genre:
        query = f"""SELECT distinct g.name, i.UnitPrice * i.Quantity as sort, c.City
                FROM tracks t
                INNER JOIN invoice_items i
                ON t.TrackId = i.TrackId
                INNER JOIN invoices ii
                ON i.InvoiceId = ii.InvoiceId
                INNER JOIN customers c
                on ii.CustomerId = c.CustomerId
                INNER JOIN genres g
                ON t.genreid = g.genreid
                WHERE g.name = '{genre}'
                ORDER by sort"""
    else:
        query = """SELECT distinct g.name, i.UnitPrice * i.Quantity as sort, c.City
                   FROM tracks t
                   INNER JOIN invoice_items i
                   ON t.TrackId = i.TrackId
                   INNER JOIN invoices ii
                   ON i.InvoiceId = ii.InvoiceId
                   INNER JOIN customers c
                   on ii.CustomerId = c.CustomerId
                   INNER JOIN genres g
                   ON t.genreid = g.genreid
                   WHERE g.name = 'Rock'
                   ORDER by sort"""
    if count:
        query += f' limit {count}'
    records = execute_query(query)
    return str(records)


app.run(debug=True, port=5000)
