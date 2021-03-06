from django.db import models


class PhoneNumber(models.Model):
	phone_number = models.CharField(max_length = 16)


class User(models.Model):
	name = models.CharField(max_length = 32)
	password = models.CharField(max_length = 16)
	registration_date = models.DateField()

	class Meta:
		abstract = True


class PetOwner(User):
	phone_number = models.OneToOneField(PhoneNumber, on_delete = models.CASCADE, related_name = 'pet_owner_name')
	breed = models.CharField(max_length = 16)
	birthday = models.DateField(null = True, blank = False)


class Clinic(User):
	phone_number = models.OneToOneField(PhoneNumber, on_delete = models.CASCADE, related_name = 'clinic_name')
	address = models.CharField(max_length = 128)
	license = models.CharField(max_length = 64)
	isVerified = models.BooleanField()


class Vet(User):
	phone_number = models.OneToOneField(PhoneNumber, on_delete = models.CASCADE, related_name = 'vet_name')
	clinic = models.ForeignKey(Clinic, on_delete = models.CASCADE)
	isVerified = models.BooleanField()


class Reminder(models.Model):
	user = models.ForeignKey(PetOwner, on_delete = models.CASCADE)
	isDeleted = models.BooleanField(default = False)
	name = models.CharField(max_length = 128)
	remarks = models.TextField(max_length = 1024)
	remain_times = models.IntegerField(default = 1 << 20)
	next_time = models.DateTimeField()
	period = models.DurationField()
	type = models.SmallIntegerField()


class SingleReminder(models.Model):
	link = models.ForeignKey(Reminder, on_delete = models.CASCADE)
	isDeleted = models.BooleanField(default = False)
	user = models.ForeignKey(PetOwner, on_delete = models.CASCADE, null = True)
	type = models.SmallIntegerField()
	time = models.DateTimeField()


class Post(models.Model):
	user = models.ForeignKey(PhoneNumber, on_delete = models.CASCADE)
	time = models.DateTimeField()
	title = models.CharField(max_length = 128)
	content = models.TextField(max_length = 4096)
	reports = models.ManyToManyField(PhoneNumber, related_name = 'reports_reports')
	likes = models.ManyToManyField(PhoneNumber, related_name = 'likes_likes')


class Reply(models.Model):
	user = models.ForeignKey(PhoneNumber, on_delete = models.CASCADE)
	thread = models.ForeignKey(Post, blank = True, null = True, on_delete = models.CASCADE)
	dependency = models.ForeignKey('self', blank = True, null = True, on_delete = models.CASCADE)
	time = models.DateTimeField()
	content = models.TextField(max_length = 2048)
	reports = models.ManyToManyField(PhoneNumber, related_name = 'reports')
	likes = models.ManyToManyField(PhoneNumber, related_name = 'likes')


class ContactRecord(models.Model):
	user = models.ForeignKey(PhoneNumber, on_delete = models.CASCADE, related_name = 'consumer')
	clinic_or_vet = models.ForeignKey(PhoneNumber, on_delete = models.CASCADE, related_name = 'producer')
	time = models.DateTimeField()
	duration = models.DurationField()


class Appointment(models.Model):
	user = models.ForeignKey(PetOwner, on_delete = models.CASCADE)
	clinic = models.ForeignKey(Clinic, on_delete = models.CASCADE)
	time = models.DateTimeField()


class PromoTips(models.Model):
	abstract = models.CharField(max_length = 128, blank = True, null = True)
	title = models.CharField(max_length = 128)
	content = models.TextField(max_length = 4096)
	time = models.DateTimeField()

	class Meta:
		abstract = True


class Promotion(PromoTips):
	user = models.ForeignKey(Clinic, on_delete = models.CASCADE)


class Tip(PromoTips):
	user = models.ForeignKey(PhoneNumber, on_delete = models.CASCADE)
