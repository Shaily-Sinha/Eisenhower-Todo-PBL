import requests
import re
import sys

BASE_URL = "http://localhost:3000"

TEST_TITLE = "Automation Test Task"
UPDATED_TITLE = "Updated Automation Test Task"


def check(condition, message):
    if condition:
        print(f"PASS: {message}")
    else:
        print(f"FAIL: {message}")
        sys.exit(1)


print("\n========================================")
print(" Eisenhower Todo - Automated API Tests")
print("========================================\n")


# --------------------------------------------------
# Test 1: Home Page
# GET /
# --------------------------------------------------

print("Test 1: GET /")

response = requests.get(BASE_URL + "/")

check(
    response.status_code == 200,
    "Home page returned HTTP 200"
)


# --------------------------------------------------
# Test 2: New Task Page
# GET /tasks/new
# --------------------------------------------------

print("\nTest 2: GET /tasks/new")

response = requests.get(BASE_URL + "/tasks/new")

check(
    response.status_code == 200,
    "New task page returned HTTP 200"
)


# --------------------------------------------------
# Test 3: Validation
# POST /tasks without title
# --------------------------------------------------

print("\nTest 3: POST /tasks - validation")

response = requests.post(
    BASE_URL + "/tasks",
    data={
        "title": "",
        "description": "Invalid test task"
    },
    allow_redirects=False
)

check(
    response.status_code == 400,
    "Empty title correctly rejected with HTTP 400"
)


# --------------------------------------------------
# Test 4: Create Task
# POST /tasks
# --------------------------------------------------

print("\nTest 4: POST /tasks - create task")

response = requests.post(
    BASE_URL + "/tasks",
    data={
        "title": TEST_TITLE,
        "description": "Created automatically by automationTesting.py",
        "isUrgent": "on",
        "isImportant": "on",
        "dueDate": "2026-12-31"
    },
    allow_redirects=False
)

check(
    response.status_code == 302,
    "Task creation returned redirect"
)


# --------------------------------------------------
# Test 5: Verify Created Task
# GET /
# --------------------------------------------------

print("\nTest 5: Verify created task")

response = requests.get(BASE_URL + "/")

check(
    TEST_TITLE in response.text,
    "Created task appears on home page"
)


# --------------------------------------------------
# Extract MongoDB Task ID from HTML
# --------------------------------------------------

match = re.search(
    r'/tasks/([a-fA-F0-9]{24})/edit',
    response.text
)

check(
    match is not None,
    "Created task ID found"
)

task_id = match.group(1)

print(f"Task ID: {task_id}")


# --------------------------------------------------
# Test 6: Edit Task Page
# GET /tasks/:id/edit
# --------------------------------------------------

print("\nTest 6: GET /tasks/:id/edit")

response = requests.get(
    f"{BASE_URL}/tasks/{task_id}/edit"
)

check(
    response.status_code == 200,
    "Edit page returned HTTP 200"
)


# --------------------------------------------------
# Test 7: Update Task
# POST /tasks/:id/update
# --------------------------------------------------

print("\nTest 7: POST /tasks/:id/update")

response = requests.post(
    f"{BASE_URL}/tasks/{task_id}/update",
    data={
        "title": UPDATED_TITLE,
        "description": "Task updated by automated testing",
        "isImportant": "on",
        "dueDate": "2027-01-15"
    },
    allow_redirects=False
)

check(
    response.status_code == 302,
    "Task update returned redirect"
)


# --------------------------------------------------
# Test 8: Verify Updated Task
# --------------------------------------------------

print("\nTest 8: Verify updated task")

response = requests.get(BASE_URL + "/")

check(
    UPDATED_TITLE in response.text,
    "Updated task appears on home page"
)


# --------------------------------------------------
# Test 9: Invalid MongoDB ID
# --------------------------------------------------

print("\nTest 9: Invalid task ID")

response = requests.get(
    BASE_URL + "/tasks/not-a-valid-id/edit"
)

check(
    response.status_code == 400,
    "Invalid task ID correctly returned HTTP 400"
)


# --------------------------------------------------
# Test 10: Delete Task
# POST /tasks/:id/delete
# --------------------------------------------------

print("\nTest 10: POST /tasks/:id/delete")

response = requests.post(
    f"{BASE_URL}/tasks/{task_id}/delete",
    allow_redirects=False
)

check(
    response.status_code == 302,
    "Task deletion returned redirect"
)


# --------------------------------------------------
# Test 11: Verify Deletion
# --------------------------------------------------

print("\nTest 11: Verify deletion")

response = requests.get(BASE_URL + "/")

check(
    UPDATED_TITLE not in response.text,
    "Deleted task no longer appears on home page"
)


print("\n========================================")
print(" ALL AUTOMATED TESTS PASSED")
print("========================================\n")