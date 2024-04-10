## Documentation

Brief overview of your Django project and its purpose.

## URL Patterns

### Django Admin Panel

- **Admin Panel:** `/admin/`
  - Description: Access the Django admin panel.

### API Endpoints

- **API:** `/api/`
  - Description: Endpoint to access application URLs defined in `drf_blog.urls`.

### User Profiles

- **Profile Information:** `/accounts/profile/`
  - Description: Endpoint to retrieve user profile information.

### Authentication and Authorization

- **Login/Logout:** `/log/`
  - Description: Endpoint to log in or log out using rest_framework.
- **Authentication:** `/authentication/`
  - Description: Endpoint for user authentication and authorization.



## Overview

Brief overview of your Django REST project and its purpose.

## URL Patterns

### Posts

- **List View:** `/posts/`
  - Description: Displays all posts.
- **Detail View:** `/posts/<int:pk>/`
  - Description: Displays details of a single post.
- **Edit View:** `/posts/<int:pk>/edit/`
  - Description: Allows editing of a specific post.
- **Delete View:** `/posts/<int:pk>/delete/`
  - Description: Allows deletion of a specific post.

### Comments

- **List/Create Comments:** `/comments/`
  - Description: Endpoint for creating a new comment or retrieving all comments.
- **Retrieve/Update/Delete Comment:** `/comments/<int:pk>/`
  - Description: Endpoint for retrieving, updating, or deleting a specific comment.
- **Edit Comment:** `/comments/<int:pk>/edit/`
  - Description: Endpoint for editing a specific comment.
- **Delete Comment:** `/comments/<int:pk>/delete/`
  - Description: Endpoint for deleting a specific comment.

## Usage

Instructions on how to use these URL patterns in your Django project.
