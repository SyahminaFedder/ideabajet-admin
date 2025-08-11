from django.db import models
from adminideabajet.models import Lokasi, Elemen1, Elemen2, Elemen3, Elemen4, Elemen5, Elemen6, Elemen7, Elemen8, Aset

class UserSubmission(models.Model):
    """Model for user budget idea submissions"""
    submission_id = models.AutoField(primary_key=True)
    
    # Demografik
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    jantina = models.CharField(max_length=20, choices=[
        ('Lelaki', 'Lelaki'),
        ('Perempuan', 'Perempuan')
    ])
    bangsa = models.CharField(max_length=20, choices=[
        ('Melayu', 'Melayu'),
        ('India', 'India'),
        ('Cina', 'Cina'),
        ('Lain-lain', 'Lain-lain')
    ])
    umur = models.CharField(max_length=20, choices=[
        ('18 - 25 tahun', '18 - 25 tahun'),
        ('26 - 39 tahun', '26 - 39 tahun'),
        ('40 - 59 tahun', '40 - 59 tahun'),
        ('60 dan ke atas', '60 dan ke atas')
    ])
    job = models.CharField(max_length=50, choices=[
        ('Ahli Majlis, MBI', 'Ahli Majlis, MBI'),
        ('Kakitangan MBI', 'Kakitangan MBI'),
        ('Kakitangan Kerajaan', 'Kakitangan Kerajaan'),
        ('Kakitangan Swasta', 'Kakitangan Swasta'),
        ('Bekerja Sendiri', 'Bekerja Sendiri'),
        ('Tidak Bekerja', 'Tidak Bekerja'),
        ('Pelajar', 'Pelajar'),
        ('Pesara', 'Pesara')
    ])
    zon = models.CharField(max_length=20, blank=True, null=True)
    
    # Cadangan
    cad = models.TextField(blank=True, null=True)
    
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ])
    
    class Meta:
        db_table = 'user_submissions'
        verbose_name = 'User Submission'
        verbose_name_plural = 'User Submissions'
    
    def __str__(self):
        return f"{self.name} - {self.submission_date}"

class SubmissionDetail(models.Model):
    """Model for submission details (pilihan, lokasi, butiran)"""
    submission = models.ForeignKey(UserSubmission, on_delete=models.CASCADE, related_name='details')
    element_number = models.IntegerField()  # 1-8 for elements
    pilihan = models.CharField(max_length=255)
    lokasi = models.CharField(max_length=255)
    butiran = models.TextField()
    
    class Meta:
        db_table = 'submission_details'
    
    def __str__(self):
        return f"{self.submission.name} - Element {self.element_number}"
