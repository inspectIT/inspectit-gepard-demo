#!/usr/bin/python

# Copyright The OpenTelemetry Authors
# SPDX-License-Identifier: Apache-2.0


import json
import os
import random
import uuid
import logging

from locust import FastHttpUser, task, constant

class PetClinicUser(FastHttpUser):
        
    # Make each user wait 5 seconds after it executed its task
    # before picking up another one
    wait_time = constant(5)
    # viewOwner task is 2x more likley to be picked up by a user than editPetType
    @task(2)
    def viewOwner(self): 
        self.client.get("/")
        self.client.get("/api/customer/owners")
        owner_id = random.randint(1, 10)
        self.client.get(f"/api/gateway/owners/{owner_id}", name="/api/gateway/owners/{ownerId}")
        self.client.get("/api/vet/vets")
    @task(1)
    def editPetType(self):
        self.client.get("/")
        self.client.get("/api/customer/owners")
        owner_id = random.randint(1, 10)
        self.client.get(f"/api/gateway/owners/{owner_id}", name="/api/gateway/owners/{ownerId}")
        pet_id = random.randint(1, 13)
        petResponse = self.client.get(f"/api/customer/owners/{owner_id}/pets/{ pet_id }", name="/api/customer/owners/{ownerId}/pets/{petId}")
        petName = petResponse.json()["name"]
        petBirthDate = petResponse.json()["birthDate"]
        petTypeResponse = self.client.get("/api/customer/petTypes")
        petTypes = petTypeResponse.json()
        random_pet_type_id = random.choice(petTypes)["id"]
        self.client.put(
            f"/api/customer/owners/{ owner_id }/pets/{ pet_id }", 
            json={"birthDate": petBirthDate, "id": pet_id, "name": petName, "typeId": random_pet_type_id}, 
            name="api/customer/owners/{ownerId}/pets/{petId}"
            )
        self.client.get("/api/customer/owners")





