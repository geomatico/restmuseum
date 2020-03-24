# REST Museum

API REST para el MCNB

## Requisitos

* Python 3.6.7 (3.5+) https://docs.djangoproject.com/en/2.2/faq/install/
* Django 2.2.3
* PostgreSQL 9.6 + PostGIS 2.2

## Puesta en marcha

Creamos un virtualenv. Podemos usar [VirtualEnvWrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

`mkvirtualenv restmuseum`

instalamos dependencias

`pip install -r requirements.pip`

> :warning: Deberemos tener la base de datos creada identica a la definida en models

Editamos el archivo `.env` con las variables adecuadas para la conexión:

| Nombre | Valor |
|---|---|
| DB_USER | museum |
| DB_PASS | museum |
| DB_HOST | 10.7.0.3 |
| DB_PORT | 5432 |
| DB_NAME | restmuseum |

ejecutamos

`source .env` (o setear las variables de entorno con otro sistema)

y arrancamos

`gunicorn -b 0.0.0.0:9999 restmuseum.wsgi`

## Modelo de datos

El modelo de datos genera esta tabla:

```sql
-- Table: public.mcnb_prod

-- DROP TABLE public.mcnb_prod;

CREATE TABLE public.mcnb_prod
(
  id SERIAL,
  typestatus character varying(255) NOT NULL,
  identificationqualifier character varying(255) NOT NULL,
  dateidentified character varying(255) NOT NULL,
  identifiedby character varying(255) NOT NULL,
  georeference_validated character varying(255) NOT NULL,
  year integer,
  month integer,
  day integer,
  maximumdepthinmeters character varying(255) NOT NULL,
  minimumdepthinmeters character varying(255) NOT NULL,
  maximumelevationinmeters character varying(255) NOT NULL,
  minimumelevationinmeters character varying(255) NOT NULL,
  individualcount character varying(255) NOT NULL,
  dayidentified character varying(255) NOT NULL,
  monthidentified character varying(255) NOT NULL,
  yearidentified character varying(255) NOT NULL,
  subspecies character varying(255) NOT NULL,
  species character varying(255) NOT NULL,
  domain character varying(255) NOT NULL,
  subspeciesid character varying(255) NOT NULL,
  speciesid character varying(255) NOT NULL,
  genusid character varying(255) NOT NULL,
  familyid character varying(255) NOT NULL,
  taxonrank character varying(255) NOT NULL,
  scientificnameauthorship character varying(255) NOT NULL,
  infraspecificepithet character varying(255) NOT NULL,
  specificepithet character varying(255) NOT NULL,
  subgenus character varying(255) NOT NULL,
  genus character varying(255) NOT NULL,
  family character varying(255) NOT NULL,
  _order character varying(255) NOT NULL,
  class character varying(255) NOT NULL,
  phylum character varying(255) NOT NULL,
  kingdom character varying(255) NOT NULL,
  scientificname character varying(255) NOT NULL,
  geodeticdatum character varying(255) NOT NULL,
  islandgroup character varying(255) NOT NULL,
  island character varying(255) NOT NULL,
  waterbody character varying(255) NOT NULL,
  verbatimlocality character varying(255) NOT NULL,
  locality character varying(255) NOT NULL,
  municipality character varying(255) NOT NULL,
  county character varying(255) NOT NULL,
  stateprovince character varying(255) NOT NULL,
  countrycode character varying(255) NOT NULL,
  country character varying(255) NOT NULL,
  continent character varying(255) NOT NULL,
  eventremarks character varying(255) NOT NULL,
  samplingprotocol character varying(255) NOT NULL,
  habitat character varying(255) NOT NULL,
  verbatimeventdate character varying(255) NOT NULL,
  eventdate character varying(255) NOT NULL,
  fieldnumber character varying(255) NOT NULL,
  occurrenceid character varying(255) NOT NULL,
  previousidentifications character varying(255) NOT NULL,
  associatedoccurrences character varying(255) NOT NULL,
  othercatalognumbers character varying(255) NOT NULL,
  associatedreferences character varying(255) NOT NULL,
  preparations character varying(255) NOT NULL,
  lifestage character varying(255) NOT NULL,
  sex character varying(255) NOT NULL,
  recordedby character varying(255) NOT NULL,
  recordnumber character varying(255) NOT NULL,
  catalognumber character varying(255) NOT NULL,
  basisofrecord character varying(255) NOT NULL,
  collectioncode character varying(255) NOT NULL,
  institutioncode character varying(255) NOT NULL,
  coordinateuncertaintyinmeters character varying(255) NOT NULL,
  decimallongitude numeric(19,10) NOT NULL,
  decimallatitude numeric(19,10) NOT NULL,
  geom geometry(Point,4326) NOT NULL,
  CONSTRAINT mcnb_prod_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.mcnb_prod
  OWNER TO museum;

-- Index: public.mcnb_prod_geom_id

-- DROP INDEX public.mcnb_prod_geom_id;

CREATE INDEX mcnb_prod_geom_id
  ON public.mcnb_prod
  USING gist
  (geom);
```

## API

### Get family and basis of record

GET `/api/v1/subtaxa/Rodentia/4/`

RESPONSE

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```
```json
[
    {
        "count": 850,
        "family": "Cricetidae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Cricetidae"
    },
    {
        "count": 609,
        "family": "Gliridae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Gliridae"
    },
    {
        "count": 449,
        "family": "Muridae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Muridae"
    },
    {
        "count": 236,
        "family": "Sciuridae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Sciuridae"
    },
    {
        "count": 6,
        "family": "",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:"
    },
    {
        "count": 5,
        "family": "Anomaluridae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Anomaluridae"
    },
    {
        "count": 3,
        "family": "Cuniculidae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Cuniculidae"
    },
    {
        "count": 2,
        "family": "Erethizontidae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Erethizontidae"
    },
    {
        "count": 2,
        "family": "Bathyergidae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Bathyergidae"
    },
    {
        "count": 1,
        "family": "Caviidae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Caviidae"
    },
    {
        "count": 1,
        "family": "Dasyproctidae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Dasyproctidae"
    },
    {
        "count": 1,
        "family": "Dipodidae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Dipodidae"
    },
    {
        "count": 1,
        "family": "Castoridae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Castoridae"
    },
    {
        "count": 1,
        "family": "Hydrochaeridae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Hydrochaeridae"
    },
    {
        "count": 1,
        "family": "Myocastoridae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Myocastoridae"
    },
    {
        "count": 1,
        "family": "Spalacidae",
        "_order": "Rodentia",
        "domain": "Eukaryota",
        "phylum": "Chordata",
        "class": "Mammalia",
        "kingdom": "Animalia",
        "familyid": "Rodentia:Spalacidae"
    }
]
```
