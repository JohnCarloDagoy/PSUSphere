"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentorg import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home
    path("", views.HomePageView.as_view(), name="home"),

    # Organization
    path("organization_list", views.OrganizationList.as_view(), name="organization-list"),
    path("organization_list/add", views.OrganizationCreateView.as_view(), name="organization-add"),
    path("organization_list/<int:pk>/edit", views.OrganizationUpdateView.as_view(), name="organization-edit"),
    path("organization_list/<int:pk>/delete", views.OrganizationDeleteView.as_view(), name="organization-delete"),

    # Org Members
    path("orgmem_list", views.OrganizationMemberList.as_view(), name="organization-member-list"),
    path("orgmem_list/add", views.OrganizationMemberCreateView.as_view(), name="organization-member-add"),
    path("orgmem_list/<int:pk>/edit", views.OrganizationMemberUpdateView.as_view(), name="organization-member-edit"),
    path("orgmem_list/<int:pk>/delete", views.OrganizationMemberDeleteView.as_view(), name="organization-member-delete"),

    # Students
    path("student_list", views.StudentListView.as_view(), name="student-list"),
    path("student_list/add", views.StudentCreateView.as_view(), name="student-add"),
    path("student_list/<int:pk>/edit", views.StudentUpdateView.as_view(), name="student-edit"),
    path("student_list/<int:pk>/delete", views.StudentDeleteView.as_view(), name="student-delete"),

    # Colleges
    path("college_list", views.CollegeListView.as_view(), name="college-list"),
    path("college_list/add", views.CollegeCreateView.as_view(), name="college-add"),
    path("college_list/<int:pk>/edit", views.CollegeUpdateView.as_view(), name="college-edit"),
    path("college_list/<int:pk>/delete", views.CollegeDeleteView.as_view(), name="college-delete"),

    # Programs
    path("program_list", views.ProgramListView.as_view(), name="program-list"),
    path("program_list/add", views.ProgramCreateView.as_view(), name="program-add"),
    path("program_list/<int:pk>/edit", views.ProgramUpdateView.as_view(), name="program-edit"),
    path("program_list/<int:pk>/delete", views.ProgramDeleteView.as_view(), name="program-delete"),
]
