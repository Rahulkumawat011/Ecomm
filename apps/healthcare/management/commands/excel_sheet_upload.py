import pandas as pd
from django.core.management.base import BaseCommand
from apps.healthcare.models import Department, Category, JobAi
import os


class Command(BaseCommand):
    help = "Imports job information from an Excel file into the database"

    def add_arguments(self, parser):
        parser.add_argument('xls_file_path', type=str, help='The path to the Excel file')

    def handle(self, *args, **options):
        xls_file_path = options['xls_file_path']

        if not os.path.exists(xls_file_path):
            self.stderr.write(self.style.ERROR(f'File not found: {xls_file_path}'))
            return

        df = pd.read_excel(xls_file_path)
        print("Excel file headers:", df.columns.tolist())

        for index, row in df.iterrows():
            department, created = Department.objects.get_or_create(
                name=row.get('Department', '')
            )

            category, created = Category.objects.get_or_create(
                name=row.get('Category', ''),
                description=row.get('Description', ''),
                department=department
            )

            JobAi.objects.create(
                department=department,
                category=category,
                description=row.get('Job Description', ''),
                roles=row.get('Roles', {}),
                skills=row.get('Skills', {})
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported job data from Excel file.'))
