from database.database import create_tables

from services.evidence_service import (
    add_evidence,
    view_all_evidence,
    search_evidence,
    delete_evidence
)

create_tables()

while True:
    print("\n==========")
    print("EVIDENCE MANAGEMENT SYSTEM")
    print("===========")

    print("1. Add Evidence")
    print("2. View Evidence")
    print("3. Search Evidence")
    print("4. Delete Evidence")
    print("5. Exit")

    choice = input(
        "\nChoose an option: "
    )

    if choice == "1":
        evidence_number = input(
            "Evidence Number: "
        )

        case_number = input(
            "Case Number: " 
        )

        description = input(
            "Description: "
        )

        location = input(
            "Storage Location: "
        )

        officer = input(
            "Receiving Officer: "
        )

        add_evidence(
            evidence_number,
            case_number,
            description,
            location,
            officer
        )

        print(
            "Evidence recorded successfully."
        )

    elif choice == "2":
        evidence = view_all_evidence()

        if evidence:
            for item in evidence:
                print(item)
        else:
            print(
                "No records found."
            )

    elif choice == "3":
        number = input(
            "Evidence Number: "
        )

        record = search_evidence(
            number
        )

        if record:
            print(record)
        else:
            print("Not found.")

    elif choice == "4":
        number = input(
            "Evidence Number: "
        )

        delete_evidence(number)

        print(
            "Evidence removed."
        )

    elif choice == "5":
        print("Goodbye.")
        break

    else:
        print(
            "Inavlid option"
        )