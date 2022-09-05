from google.cloud import datastore


def migrate_kind(kind, project_id_from, project_id_to):
    client_odp = datastore.Client(project=project_id_from)
    client_cse = datastore.Client(project=project_id_to)

    query = client_odp.query(kind=kind)
    l = query.fetch()
    l = list(l)
    if not l:
        print("No entity found")
    else:  
        print(f"Found {len(l)} entities")
        client_cse.put(l)

    print(f"Finished migrating {kind}")


if __name__ == "__main__":
    kind = input("Enter kind value: ")
    project_id_from = input("Enter project_id_from value: ")
    project_id_to = input("Enter project_id_to value: ")

    migrate_kind(kind, project_id_from, project_id_to)