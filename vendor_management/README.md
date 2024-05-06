
# Vendor management API

A brief description of what this project does.


## Initial setup

To set-up the project in local env install

```bash
pip install -r requirements.txt
```

After installing provided dependencies.

To set-up local database use commands
```
python3 manage.py makemigrations
python3 manage.py migrate
```
Create a superuser to login and use token authentication.
```
python3 manage.py createsuperuser
```

Run the server 
```
python3 manage.py runserver
```

Use swagger url for better user interaction
```
http://127.0.0.1:8000/swagger/
```

To login through swagger authorize, login with Admin credentials and login in token auth url

For authentication add - " Bearer {your access token} "


## API Reference

#### Get all vendors

```http
GET /api/vendors/
```

#### To create vendor

```http
POST /api/vendors/
```

#### Get vendor

```http
GET /api/vendors/<str:vendor_id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `vendor_id`      | `string` | **Required**. Id of the vendor    |

#### update vendor

```http
PUT /api/vendors/<str:vendor_id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `vendor_id`| `string` | **Required**. id of the vendor    |

#### delete vendor

```http
delete /api/vendors/<str:vendor_id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of the vendor    |


#### Get all Purchase orders

```http
GET /api/purchase_orders/
```

#### To create vendor

```http
POST /api/purchase_orders/
```

#### Get single purchase order
```http
GET /api/purchase_orders/<str:po_id>/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `po_id`   | `string` | **Required**. id of the purchase order |

#### Update single purchase order
```http
PUT /api/purchase_orders/<str:po_id>/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `po_id`   | `string` | **Required**. id of the purchase order |

#### Delete purchase order
```http
DELETE /api/purchase_orders/<str:po_id>/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `po_id`   | `string` | **Required**. id of the purchase order |

#### To get vendor performance
```http
GET /api/vendors/<str:vendor_id>/performance/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `vendor_id`| `string` | **Required**. id of the vendor    |

#### get access to auth token
```http
GET api/token/
```
#### get access to refresh token
```http
GET api/token/refresh/
```

