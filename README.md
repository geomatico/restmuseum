# REST Museum

API REST para el museo

## Conexión a la base de datos

Crear un archivo `.env` con las variables para la conexión:

| Nombre | Valor |
|---|---|
| DB_USER | museum |
| DB_PASS | museum |
| DB_HOST | 10.7.0.3 |
| DB_PORT | 5432 |
| DB_NAME | restmuseum |

y ejecutar

`source .env`

El modelo de datos genera esta tabla:

```sql
-- Table: public.api_mcbnprod

-- DROP TABLE public.api_mcbnprod;

CREATE TABLE public.api_mcbnprod
(
  id integer NOT NULL DEFAULT nextval('api_mcbnprod_id_seq'::regclass),
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
  _class character varying(255) NOT NULL,
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
  CONSTRAINT api_mcbnprod_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.api_mcbnprod
  OWNER TO museum;

-- Index: public.api_mcbnprod_geom_id

-- DROP INDEX public.api_mcbnprod_geom_id;

CREATE INDEX api_mcbnprod_geom_id
  ON public.api_mcbnprod
  USING gist
  (geom);
```

> :warning: Cualquier diferencia con la tabla actual habrá que actualizar el modelo




