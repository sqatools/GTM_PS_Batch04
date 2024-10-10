
protocol ="https"
server ="api.restful-api.dev"

create_object_payload = {
   "name": "Apple MacBook Pro 120",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

json_headers = {
            'Content-Type': 'application/json'
        }


update_data_info_for_object_id = {
   "name": "Apple MacBook Pro 150",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "2 TB"
   }
}


update_specific_data_for_object = {"data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "5 TB"
   }
}
