def automation():
    # Step 1: Read input
    data = get_input()

    # Step 2: Validate
    if not validate(data):
        return "Invalid Input"

    # Step 3: Process
    result = process(data)

    # Step 4: Decision
    if result["status"] == "success":
        save_result(result)
        send_notification("Completed Successfully")
    else:
        log_error(result)
        send_notification("Failed")

    return result

if __name__ == "__main__":
    automation()
    