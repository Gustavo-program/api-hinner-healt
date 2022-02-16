from django.db import models
from authentication.models import InnerHealthAbstractClass
from django.contrib.auth.models import User


class Especiality(InnerHealthAbstractClass):
    class Meta:
        verbose_name = "Especiality"
        verbose_name_plural = "Especialities"

    name = models.CharField(
        max_length=250,
        verbose_name=("Name")
    )

    def __str__(self):
        return self.name


class Patient(InnerHealthAbstractClass):
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    user = models.OneToOneField(
        User,
        related_name='user_patient',
        on_delete=models.CASCADE,
        verbose_name=("User")
    )
    phone = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=("Phone")
    )
    age = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        verbose_name=("Age")
    )
    weight = models.CharField(
        max_length=5,
        blank=True,
        null=True,
        verbose_name=("Weight")
    )
    stature = models.CharField(
        max_length=5,
        blank=True,
        null=True,
        verbose_name=("Stature")
    )

    district = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=("District")
    )
    residence = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=("Residence")
    )

    def __str__(self):
        return self.user.first_name


class Testimonial(InnerHealthAbstractClass):
    class Meta:
        verbose_name = "Testimony"
        verbose_name_plural = "Testimonials"

    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=("User")
    )
    testimony = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name=("Testimony")
    )

    def __str__(self):
        return self.user.first_name


class Doctor(InnerHealthAbstractClass):
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    user = models.OneToOneField(
        User,
        related_name='user_doctor',
        on_delete=models.CASCADE,
        verbose_name=("User")
    )
    especiality = models.ForeignKey(
        Especiality,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=("Especiality")
    )
    phone = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=("Phone")
    )

    def __str__(self):
        return self.user.first_name


class Appointment(InnerHealthAbstractClass):
    _APPOINTMENT_STATES = (
        ('REQUESTED', 'SOLICITADA'),
        ('REJECTED', 'RECHAZADA'),
        ('ACCEPTED', 'ACEPTADA'),
    )

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

    motive = models.TextField(
        null=True
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        verbose_name=("Doctor")
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=("Patient")
    )
    state = models.CharField(
        max_length=25,
        choices=_APPOINTMENT_STATES,
        default='REQUESTED',
        verbose_name=("State")
    )
    due_date = models.DateTimeField(
        verbose_name=("Due date")
    )

    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name} Patient: {self.patient.user.username}"

    def save(self, *args, **kwargs):
        existent_appointment = self.__class__.objects.filter(
            doctor=self.doctor,
            due_date=self.due_date
        ).exclude(id=self.pk)

        if existent_appointment:
            raise Exception(
                "El doctor ya tiene una cita programada para esa fecha")

        super(Appointment, self).save(*args, **kwargs)
