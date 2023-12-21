from const import collection

import streamlit as st

def migration():
    st.write("Migrating data to MongoDB...")
    collection.insert_many([
        { "name": "John Doe", "email": "john.doe@example.com", "address": "123 Main St", "phone": "555-1234", "age": 25 },
        { "name": "Jane Smith", "email": "jane.smith@example.com", "address": "456 Elm St", "phone": "555-5678", "age": 30 },
        { "name": "Bob Johnson", "email": "bob.johnson@example.com", "address": "789 Oak St", "phone": "555-9012", "age": 35 },
        { "name": "Alice Williams", "email": "alice.williams@example.com", "address": "321 Pine St", "phone": "555-3456", "age": 25 },
        { "name": "Mike Brown", "email": "mike.brown@example.com", "address": "654 Cedar St", "phone": "555-7890", "age": 30 },
        { "name": "Sarah Davis", "email": "sarah.davis@example.com", "address": "987 Maple St", "phone": "555-2345", "age": 35 },
        { "name": "Tom Wilson", "email": "tom.wilson@example.com", "address": "123 Oak St", "phone": "555-6789", "age": 25 },
        { "name": "Emily Taylor", "email": "emily.taylor@example.com", "address": "456 Pine St", "phone": "555-0123", "age": 30 },
        { "name": "Chris Anderson", "email": "chris.anderson@example.com", "address": "789 Cedar St", "phone": "555-4567", "age": 35 },
        { "name": "Olivia Martinez", "email": "olivia.martinez@example.com", "address": "321 Elm St", "phone": "555-8901", "age": 25 },
        { "name": "Daniel Clark", "email": "daniel.clark@example.com", "address": "654 Oak St", "phone": "555-2345", "age": 30 },
        { "name": "Sophia Rodriguez", "email": "sophia.rodriguez@example.com", "address": "987 Pine St", "phone": "555-6789", "age": 35 },
        { "name": "Matthew Lee", "email": "matthew.lee@example.com", "address": "123 Cedar St", "phone": "555-0123", "age": 25 },
        { "name": "Ava Harris", "email": "ava.harris@example.com", "address": "456 Elm St", "phone": "555-4567", "age": 30 },
        { "name": "Andrew Lewis", "email": "andrew.lewis@example.com", "address": "789 Oak St", "phone": "555-8901", "age": 35 },
        { "name": "Isabella Young", "email": "isabella.young@example.com", "address": "321 Pine St", "phone": "555-2345", "age": 25 },
        { "name": "Joseph Hall", "email": "joseph.hall@example.com", "address": "654 Cedar St", "phone": "555-6789", "age": 30 },
        { "name": "Mia Allen", "email": "mia.allen@example.com", "address": "987 Maple St", "phone": "555-0123", "age": 35 },
        { "name": "David Green", "email": "david.green@example.com", "address": "123 Oak St", "phone": "555-4567", "age": 25 },
        { "name": "Emma Baker", "email": "emma.baker@example.com", "address": "456 Pine St", "phone": "555-8901", "age": 30 },
        { "name": "Benjamin King", "email": "benjamin.king@example.com", "address": "789 Cedar St", "phone": "555-2345", "age": 35 },
        { "name": "Chloe Wright", "email": "chloe.wright@example.com", "address": "321 Elm St", "phone": "555-6789", "age": 25 },
        { "name": "James Scott", "email": "james.scott@example.com", "address": "654 Oak St", "phone": "555-0123", "age": 30 },
        { "name": "Lily Torres", "email": "lily.torres@example.com", "address": "987 Pine St", "phone": "555-4567", "age": 35 },
        { "name": "Michael Ramirez", "email": "michael.ramirez@example.com", "address": "123 Cedar St", "phone": "555-8901", "age": 25 },
        { "name": "Grace Peterson", "email": "grace.peterson@example.com", "address": "456 Elm St", "phone": "555-2345", "age": 30 },
        { "name": "Samantha Gray", "email": "samantha.gray@example.com", "address": "789 Oak St", "phone": "555-6789", "age": 35 },
        { "name": "Henry Cook", "email": "henry.cook@example.com", "address": "321 Pine St", "phone": "555-0123", "age": 25 },
        { "name": "Victoria Bell", "email": "victoria.bell@example.com", "address": "654 Cedar St", "phone": "555-4567", "age": 30 },
        { "name": "Andrew Reed", "email": "andrew.reed@example.com", "address": "987 Maple St", "phone": "555-8901", "age": 35 },
    ], ordered=False)
    st.write("Migrated!")

st.button("Migrate", on_click=migration)
