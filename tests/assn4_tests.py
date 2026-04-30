# import pytest
# import requests

# # ---------------------------------------------------------------------------
# # Service URLs
# # ---------------------------------------------------------------------------
# STORE1 = "http://localhost:5001"
# STORE2 = "http://localhost:5002"
# ORDER  = "http://localhost:5003"

# # ---------------------------------------------------------------------------
# # Pet type payloads
# # ---------------------------------------------------------------------------
# PET_TYPE1 = {"type": "Golden Retriever"}
# PET_TYPE2 = {"type": "Australian Shepherd"}
# PET_TYPE3 = {"type": "Abyssinian"}
# PET_TYPE4 = {"type": "bulldog"}

# # ---------------------------------------------------------------------------
# # Expected values (attributes stored lowercase by the app)
# # ---------------------------------------------------------------------------
# PET_TYPE1_VAL = {
#     "type":       "Golden Retriever",
#     "family":     "Canidae",
#     "genus":      "Canis",
#     "attributes": [],
#     "lifespan":   12
# }
# PET_TYPE2_VAL = {
#     "type":       "Australian Shepherd",
#     "family":     "Canidae",
#     "genus":      "Canis",
#     "attributes": ["loyal", "outgoing", "and", "friendly"],
#     "lifespan":   15
# }
# PET_TYPE3_VAL = {
#     "type":       "Abyssinian",
#     "family":     "Felidae",
#     "genus":      "Felis",
#     "attributes": ["intelligent", "and", "curious"],
#     "lifespan":   13
# }
# PET_TYPE4_VAL = {
#     "type":       "bulldog",
#     "family":     "Canidae",
#     "genus":      "Canis",
#     "attributes": ["gentle", "calm", "and", "affectionate"],
#     "lifespan":   None
# }

# # ---------------------------------------------------------------------------
# # Pet payloads
# # ---------------------------------------------------------------------------
# PET1_TYPE1 = {"name": "Lander",  "birthdate": "14-05-2020"}
# PET2_TYPE1 = {"name": "Lanky"}
# PET3_TYPE1 = {"name": "Shelly",  "birthdate": "07-07-2019"}
# PET4_TYPE2 = {"name": "Felicity","birthdate": "27-11-2011"}
# PET5_TYPE3 = {"name": "Muscles"}
# PET6_TYPE3 = {"name": "Junior"}
# PET7_TYPE4 = {"name": "Lazy",    "birthdate": "07-08-2018"}
# PET8_TYPE4 = {"name": "Lemon",   "birthdate": "27-03-2020"}

# # ---------------------------------------------------------------------------
# # Shared state – populated by early tests, used by later tests
# # ---------------------------------------------------------------------------
# ids = {}   # id_1 ... id_6


# # ===========================================================================
# # Tests 1 & 2 – POST /pet-types
# # ===========================================================================

# def test_1_post_pet_types_store1():
#     """POST PET_TYPE1, PET_TYPE2, PET_TYPE3 to pet-store #1."""
#     payloads = [PET_TYPE1, PET_TYPE2, PET_TYPE3]
#     vals     = [PET_TYPE1_VAL, PET_TYPE2_VAL, PET_TYPE3_VAL]
#     responses = []

#     for payload in payloads:
#         r = requests.post(f"{STORE1}/pet-types", json=payload)
#         responses.append(r)

#     # Status codes must all be 201
#     for r in responses:
#         assert r.status_code == 201, \
#             f"Expected 201, got {r.status_code} for {r.request.body}"

#     # Store IDs
#     ids['id_1'] = responses[0].json()['id']
#     ids['id_2'] = responses[1].json()['id']
#     ids['id_3'] = responses[2].json()['id']

#     # IDs must be unique within store 1
#     store1_ids = [ids['id_1'], ids['id_2'], ids['id_3']]
#     assert len(set(store1_ids)) == 3, "IDs returned for store 1 are not unique"

#     # Family and genus must match expected values
#     for r, val in zip(responses, vals):
#         data = r.json()
#         assert data['family'].lower() == val['family'].lower(), \
#             f"family mismatch: got {data['family']}, expected {val['family']}"
#         assert data['genus'].lower() == val['genus'].lower(), \
#             f"genus mismatch: got {data['genus']}, expected {val['genus']}"


# def test_2_post_pet_types_store2():
#     """POST PET_TYPE1, PET_TYPE2, PET_TYPE4 to pet-store #2."""
#     payloads = [PET_TYPE1, PET_TYPE2, PET_TYPE4]
#     vals     = [PET_TYPE1_VAL, PET_TYPE2_VAL, PET_TYPE4_VAL]
#     responses = []

#     for payload in payloads:
#         r = requests.post(f"{STORE2}/pet-types", json=payload)
#         responses.append(r)

#     # Status codes must all be 201
#     for r in responses:
#         assert r.status_code == 201, \
#             f"Expected 201, got {r.status_code} for {r.request.body}"

#     # Store IDs
#     ids['id_4'] = responses[0].json()['id']
#     ids['id_5'] = responses[1].json()['id']
#     ids['id_6'] = responses[2].json()['id']

#     # IDs must be unique within store 2
#     store2_ids = [ids['id_4'], ids['id_5'], ids['id_6']]
#     assert len(set(store2_ids)) == 3, "IDs returned for store 2 are not unique"

#     # Family and genus must match expected values
#     for r, val in zip(responses, vals):
#         data = r.json()
#         assert data['family'].lower() == val['family'].lower(), \
#             f"family mismatch: got {data['family']}, expected {val['family']}"
#         assert data['genus'].lower() == val['genus'].lower(), \
#             f"genus mismatch: got {data['genus']}, expected {val['genus']}"


# # ===========================================================================
# # Tests 3 & 4 – POST /pet-types/{id}/pets to store 1
# # ===========================================================================

# def test_3_post_pets_store1_type1():
#     """POST PET1_TYPE1 and PET2_TYPE1 to store 1 / id_1 (Golden Retriever)."""
#     for pet in [PET1_TYPE1, PET2_TYPE1]:
#         r = requests.post(f"{STORE1}/pet-types/{ids['id_1']}/pets", json=pet)
#         assert r.status_code == 201, \
#             f"Expected 201, got {r.status_code} posting {pet}"


# def test_4_post_pets_store1_type3():
#     """POST PET5_TYPE3 and PET6_TYPE3 to store 1 / id_3 (Abyssinian)."""
#     for pet in [PET5_TYPE3, PET6_TYPE3]:
#         r = requests.post(f"{STORE1}/pet-types/{ids['id_3']}/pets", json=pet)
#         assert r.status_code == 201, \
#             f"Expected 201, got {r.status_code} posting {pet}"


# # ===========================================================================
# # Tests 5, 6, 7 – POST /pet-types/{id}/pets to store 2
# # ===========================================================================

# def test_5_post_pets_store2_type1():
#     """POST PET3_TYPE1 to store 2 / id_4 (Golden Retriever)."""
#     r = requests.post(f"{STORE2}/pet-types/{ids['id_4']}/pets", json=PET3_TYPE1)
#     assert r.status_code == 201, f"Expected 201, got {r.status_code}"


# def test_6_post_pets_store2_type2():
#     """POST PET4_TYPE2 to store 2 / id_5 (Australian Shepherd)."""
#     r = requests.post(f"{STORE2}/pet-types/{ids['id_5']}/pets", json=PET4_TYPE2)
#     assert r.status_code == 201, f"Expected 201, got {r.status_code}"


# def test_7_post_pets_store2_type4():
#     """POST PET7_TYPE4 and PET8_TYPE4 to store 2 / id_6 (bulldog)."""
#     for pet in [PET7_TYPE4, PET8_TYPE4]:
#         r = requests.post(f"{STORE2}/pet-types/{ids['id_6']}/pets", json=pet)
#         assert r.status_code == 201, \
#             f"Expected 201, got {r.status_code} posting {pet}"


# # ===========================================================================
# # Test 8 – GET /pet-types/{id_2} from store 1
# # ===========================================================================

# def test_8_get_pet_type_store1():
#     """GET /pet-types/{id_2} from store 1 and verify against PET_TYPE2_VAL."""
#     r = requests.get(f"{STORE1}/pet-types/{ids['id_2']}")
#     assert r.status_code == 200, f"Expected 200, got {r.status_code}"

#     data = r.json()

#     assert data['type'].lower() == PET_TYPE2_VAL['type'].lower(), \
#         f"type mismatch: {data['type']}"
#     assert data['family'].lower() == PET_TYPE2_VAL['family'].lower(), \
#         f"family mismatch: {data['family']}"
#     assert data['genus'].lower() == PET_TYPE2_VAL['genus'].lower(), \
#         f"genus mismatch: {data['genus']}"
#     assert data['lifespan'] == PET_TYPE2_VAL['lifespan'], \
#         f"lifespan mismatch: {data['lifespan']}"

#     # Attributes – compare as sets, case-insensitive
#     expected_attrs = set(a.lower() for a in PET_TYPE2_VAL['attributes'])
#     actual_attrs   = set(a.lower() for a in data.get('attributes', []))
#     assert expected_attrs == actual_attrs, \
#         f"attributes mismatch: got {actual_attrs}, expected {expected_attrs}"


# # ===========================================================================
# # Test 9 – GET /pet-types/{id_6}/pets from store 2
# # ===========================================================================

# def test_9_get_pets_store2_type4():
#     """GET /pet-types/{id_6}/pets from store 2 and verify PET7/PET8_TYPE4."""
#     r = requests.get(f"{STORE2}/pet-types/{ids['id_6']}/pets")
#     assert r.status_code == 200, f"Expected 200, got {r.status_code}"

#     pets = r.json()
#     assert isinstance(pets, list), "Response should be a JSON array"

#     # Build a name → pet dict for easy lookup (case-insensitive)
#     pets_by_name = {p['name'].lower(): p for p in pets}

#     for expected_pet in [PET7_TYPE4, PET8_TYPE4]:
#         name_key = expected_pet['name'].lower()
#         assert name_key in pets_by_name, \
#             f"Pet '{expected_pet['name']}' not found in response"

#         actual = pets_by_name[name_key]

#         if 'birthdate' in expected_pet:
#             assert actual['birthdate'] == expected_pet['birthdate'], \
#                 f"birthdate mismatch for {expected_pet['name']}: " \
#                 f"got {actual['birthdate']}, expected {expected_pet['birthdate']}"

# - Tester test file -

import pytest
import requests
import json

# Base URLs for the pet store instances
PET_STORE_1_URL = "http://localhost:5001"
PET_STORE_2_URL = "http://localhost:5002"
PET_ORDER_URL = "http://localhost:5003"

# Pet Type Payloads
PET_TYPE1 = {
    "type": "Golden Retriever"
}

PET_TYPE2 = {
    "type": "Australian Shepherd"
}

PET_TYPE3 = {
    "type": "Abyssinian"
}

PET_TYPE4 = {
    "type": "bulldog"
}

# Expected Pet Type Values
PET_TYPE1_VAL = {
    "type": "Golden Retriever",
    "family": "Canidae",
    "genus": "Canis",
    "attributes": [],
    "lifespan": 12
}

PET_TYPE2_VAL = {
    "type": "Australian Shepherd",
    "family": "Canidae",
    "genus": "Canis",
    "attributes": ["Loyal", "outgoing", "and", "friendly"],
    "lifespan": 15
}

PET_TYPE3_VAL = {
    "type": "Abyssinian",
    "family": "Felidae",
    "genus": "Felis",
    "attributes": ["Intelligent", "and", "curious"],
    "lifespan": 13
}

PET_TYPE4_VAL = {
    "type": "bulldog",
    "family": "Canidae",
    "genus": "Canis",
    "attributes": ["Gentle", "calm", "and", "affectionate"],
    "lifespan": None
}

# Pet Payloads
PET1_TYPE1 = {
    "name": "Lander",
    "birthdate": "14-05-2020"
}

PET2_TYPE1 = {
    "name": "Lanky"
}

PET3_TYPE1 = {
    "name": "Shelly",
    "birthdate": "07-07-2019"
}

PET4_TYPE2 = {
    "name": "Felicity",
    "birthdate": "27-11-2011"
}

PET5_TYPE3 = {
    "name": "Muscles"
}

PET6_TYPE3 = {
    "name": "Junior"
}

PET7_TYPE4 = {
    "name": "Lazy",
    "birthdate": "07-08-2018"
}

PET8_TYPE4 = {
    "name": "Lemon",
    "birthdate": "27-03-2020"
}

# Global variables to store IDs
pet_type_ids = {}


class TestPetStoreSetup:
    """Test 1-2: POST pet-types to both stores and verify unique IDs and correct values"""
    
    def test_01_post_pet_types_to_store1(self):
        """Test 1: POST 3 pet-types to pet-store #1 (PET_TYPE1, PET_TYPE2, PET_TYPE3)"""
        global pet_type_ids
        
        # POST PET_TYPE1
        response1 = requests.post(f"{PET_STORE_1_URL}/pet-types", json=PET_TYPE1)
        assert response1.status_code == 201, f"Expected 201, got {response1.status_code}"
        data1 = response1.json()
        id_1 = data1["id"]
        assert data1["family"] == PET_TYPE1_VAL["family"]
        assert data1["genus"] == PET_TYPE1_VAL["genus"]
        
        # POST PET_TYPE2
        response2 = requests.post(f"{PET_STORE_1_URL}/pet-types", json=PET_TYPE2)
        assert response2.status_code == 201, f"Expected 201, got {response2.status_code}"
        data2 = response2.json()
        id_2 = data2["id"]
        assert data2["family"] == PET_TYPE2_VAL["family"]
        assert data2["genus"] == PET_TYPE2_VAL["genus"]
        
        # POST PET_TYPE3
        response3 = requests.post(f"{PET_STORE_1_URL}/pet-types", json=PET_TYPE3)
        assert response3.status_code == 201, f"Expected 201, got {response3.status_code}"
        data3 = response3.json()
        id_3 = data3["id"]
        assert data3["family"] == PET_TYPE3_VAL["family"]
        assert data3["genus"] == PET_TYPE3_VAL["genus"]
        
        # Verify all IDs are unique
        assert id_1 != id_2 != id_3, "IDs must be unique"
        
        # Store IDs for later tests
        pet_type_ids['id_1'] = id_1
        pet_type_ids['id_2'] = id_2
        pet_type_ids['id_3'] = id_3
    
    def test_02_post_pet_types_to_store2(self):
        """Test 2: POST 3 pet-types to pet-store #2 (PET_TYPE1, PET_TYPE2, PET_TYPE4)"""
        global pet_type_ids
        
        # POST PET_TYPE1
        response4 = requests.post(f"{PET_STORE_2_URL}/pet-types", json=PET_TYPE1)
        assert response4.status_code == 201, f"Expected 201, got {response4.status_code}"
        data4 = response4.json()
        id_4 = data4["id"]
        assert data4["family"] == PET_TYPE1_VAL["family"]
        assert data4["genus"] == PET_TYPE1_VAL["genus"]
        
        # POST PET_TYPE2
        response5 = requests.post(f"{PET_STORE_2_URL}/pet-types", json=PET_TYPE2)
        assert response5.status_code == 201, f"Expected 201, got {response5.status_code}"
        data5 = response5.json()
        id_5 = data5["id"]
        assert data5["family"] == PET_TYPE2_VAL["family"]
        assert data5["genus"] == PET_TYPE2_VAL["genus"]
        
        # POST PET_TYPE4
        response6 = requests.post(f"{PET_STORE_2_URL}/pet-types", json=PET_TYPE4)
        assert response6.status_code == 201, f"Expected 201, got {response6.status_code}"
        data6 = response6.json()
        id_6 = data6["id"]
        assert data6["family"] == PET_TYPE4_VAL["family"]
        assert data6["genus"] == PET_TYPE4_VAL["genus"]
        
        # Verify all IDs are unique
        assert id_4 != id_5 != id_6, "IDs must be unique"
        
        # Store IDs for later tests
        pet_type_ids['id_4'] = id_4
        pet_type_ids['id_5'] = id_5
        pet_type_ids['id_6'] = id_6


class TestPetCreation:
    """Tests 3-7: POST pets to various pet-types"""
    
    def test_03_post_pets_to_store1_type1(self):
        """Test 3: POST 2 pets to pet-store #1 pet-type id_1 (Golden Retriever)"""
        id_1 = pet_type_ids['id_1']
        
        # POST PET1_TYPE1
        response1 = requests.post(f"{PET_STORE_1_URL}/pet-types/{id_1}/pets", json=PET1_TYPE1)
        assert response1.status_code == 201, f"Expected 201, got {response1.status_code}"
        
        # POST PET2_TYPE1
        response2 = requests.post(f"{PET_STORE_1_URL}/pet-types/{id_1}/pets", json=PET2_TYPE1)
        assert response2.status_code == 201, f"Expected 201, got {response2.status_code}"
    
    def test_04_post_pets_to_store1_type3(self):
        """Test 4: POST 2 pets to pet-store #1 pet-type id_3 (Abyssinian)"""
        id_3 = pet_type_ids['id_3']
        
        # POST PET5_TYPE3
        response1 = requests.post(f"{PET_STORE_1_URL}/pet-types/{id_3}/pets", json=PET5_TYPE3)
        assert response1.status_code == 201, f"Expected 201, got {response1.status_code}"
        
        # POST PET6_TYPE3
        response2 = requests.post(f"{PET_STORE_1_URL}/pet-types/{id_3}/pets", json=PET6_TYPE3)
        assert response2.status_code == 201, f"Expected 201, got {response2.status_code}"
    
    def test_05_post_pet_to_store2_type1(self):
        """Test 5: POST 1 pet to pet-store #2 pet-type id_4 (Golden Retriever)"""
        id_4 = pet_type_ids['id_4']
        
        # POST PET3_TYPE1
        response = requests.post(f"{PET_STORE_2_URL}/pet-types/{id_4}/pets", json=PET3_TYPE1)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    
    def test_06_post_pet_to_store2_type2(self):
        """Test 6: POST 1 pet to pet-store #2 pet-type id_5 (Australian Shepherd)"""
        id_5 = pet_type_ids['id_5']
        
        # POST PET4_TYPE2
        response = requests.post(f"{PET_STORE_2_URL}/pet-types/{id_5}/pets", json=PET4_TYPE2)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    
    def test_07_post_pets_to_store2_type4(self):
        """Test 7: POST 2 pets to pet-store #2 pet-type id_6 (bulldog)"""
        id_6 = pet_type_ids['id_6']
        
        # POST PET7_TYPE4
        response1 = requests.post(f"{PET_STORE_2_URL}/pet-types/{id_6}/pets", json=PET7_TYPE4)
        assert response1.status_code == 201, f"Expected 201, got {response1.status_code}"
        
        # POST PET8_TYPE4
        response2 = requests.post(f"{PET_STORE_2_URL}/pet-types/{id_6}/pets", json=PET8_TYPE4)
        assert response2.status_code == 201, f"Expected 201, got {response2.status_code}"


class TestPetTypeRetrieval:
    """Test 8: GET specific pet-type and verify all fields"""
    
    def test_08_get_pet_type_from_store1(self):
        """Test 8: GET /pet-types/{id_2} from pet-store #1 and verify all fields"""
        id_2 = pet_type_ids['id_2']
        
        response = requests.get(f"{PET_STORE_1_URL}/pet-types/{id_2}")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        data = response.json()
        
        # Verify all fields match PET_TYPE2_VAL
        assert data["type"].lower() == PET_TYPE2_VAL["type"].lower()
        assert data["family"] == PET_TYPE2_VAL["family"]
        assert data["genus"] == PET_TYPE2_VAL["genus"]
        assert data["attributes"] == PET_TYPE2_VAL["attributes"]
        assert data["lifespan"] == PET_TYPE2_VAL["lifespan"]


class TestPetsRetrieval:
    """Test 9: GET pets of a specific type and verify"""
    
    def test_09_get_pets_from_store2_type4(self):
        """Test 9: GET /pet-types/{id_6}/pets from pet-store #2 and verify pets"""
        id_6 = pet_type_ids['id_6']
        
        response = requests.get(f"{PET_STORE_2_URL}/pet-types/{id_6}/pets")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        data = response.json()
        
        # Verify it's an array with 2 pets
        assert isinstance(data, list), "Response should be an array"
        assert len(data) == 2, f"Expected 2 pets, got {len(data)}"
        
        # Extract pet names
        pet_names = [pet["name"].lower() for pet in data]
        
        # Verify both pets are present
        assert "lazy" in pet_names, "Pet 'Lazy' should be in the list"
        assert "lemon" in pet_names, "Pet 'Lemon' should be in the list"
        
        # Verify birthdates
        for pet in data:
            if pet["name"].lower() == "lazy":
                assert pet["birthdate"] == PET7_TYPE4["birthdate"]
            elif pet["name"].lower() == "lemon":
                assert pet["birthdate"] == PET8_TYPE4["birthdate"]


class TestQueryStrings:
    """Test 10: Additional test for query string functionality"""
    
    def test_10_query_by_family(self):
        """Test 10: GET /pet-types with query string family=Canidae from both stores"""
        
        # Query store 1
        response1 = requests.get(f"{PET_STORE_1_URL}/pet-types?family=Canidae")
        assert response1.status_code == 200, f"Expected 200, got {response1.status_code}"
        data1 = response1.json()
        assert isinstance(data1, list), "Response should be an array"
        # Store 1 should have 2 Canidae types (Golden Retriever, Australian Shepherd)
        assert len(data1) == 2, f"Expected 2 Canidae types in store 1, got {len(data1)}"
        
        # Query store 2
        response2 = requests.get(f"{PET_STORE_2_URL}/pet-types?family=Canidae")
        assert response2.status_code == 200, f"Expected 200, got {response2.status_code}"
        data2 = response2.json()
        assert isinstance(data2, list), "Response should be an array"
        # Store 2 should have 3 Canidae types (Golden Retriever, Australian Shepherd, bulldog)
        assert len(data2) == 3, f"Expected 3 Canidae types in store 2, got {len(data2)}"
