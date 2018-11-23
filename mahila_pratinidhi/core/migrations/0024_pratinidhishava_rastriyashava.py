# Generated by Django 2.0.7 on 2018-10-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20181003_0742'),
    ]

    operations = [
        migrations.CreateModel(
            name='PratinidhiShava',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='नाम')),
                ('english_name', models.CharField(max_length=300, verbose_name='English Name')),
                ('date_of_birth', models.CharField(max_length=300, verbose_name='जन्ममिती')),
                ('mothers_name', models.CharField(max_length=300, verbose_name='आमाको नाम')),
                ('fathers_name', models.CharField(max_length=300, verbose_name='बाबुको नाम')),
                ('marital_status', models.CharField(blank=True, max_length=300, null=True, verbose_name='बैवाहिक स्थिथि')),
                ('updated_marital_status', models.CharField(blank=True, choices=[('cljjflxt', 'अविवाहित'), ('ljjflxt', 'विवाहित'), ('Psn', 'एकल'), ('cGo', 'अन्य')], max_length=300, null=True, verbose_name='बैवाहिक स्थिथि')),
                ('husbands_name', models.CharField(max_length=300, verbose_name='श्रीमानको नाम')),
                ('caste', models.CharField(blank=True, max_length=300, null=True, verbose_name='जातियता')),
                ('updated_caste', models.CharField(blank=True, choices=[('blnt', 'दलित'), ('cflbaf;L÷hghftL', 'आदिबासी / जनजाती'), ('v; cfo{', 'खस आर्य'), ('dw];L ', 'मधेसी'), ('yf?', 'थारु'), ('d"l:nd', 'मुस्लिम'), ('cGo', 'अन्य')], max_length=300, null=True, verbose_name='जातियता')),
                ('mother_tongue', models.CharField(blank=True, max_length=300, null=True, verbose_name='मातृभाषा')),
                ('updated_mother_tongue', models.CharField(blank=True, choices=[('नेपाली', 'नेपाली'), ('मगर खामस्तानाकोतरराजनीति शास्त्र', 'मगर खामस्तानाकोतरराजनीति शास्त्र'), ('नेवारी', 'नेवारी'), ('नेपाल भाषा', 'नेपाल भाषा'), ('तामाङ', 'तामाङ')], max_length=300, null=True, verbose_name='मातृभाषा')),
                ('educational_qualification', models.CharField(blank=True, max_length=300, null=True, verbose_name='औपचारिक शैक्षिक योग्यता')),
                ('updated_educational_qualification', models.CharField(blank=True, choices=[('lg/If/', 'निरक्षर'), (';fIf/', 'साक्षर'), ('P;=Pn=;L= ', 'एस.एल.सी.'), ('!) @ jf ;f] ;/x', '१० + २ वा सो सरह'), (':gfts', 'स्नातक'), (':gfsf]]t/', 'स्नाकोतर'), ('lk=Pr=8L=', 'पि.एच.डी')], max_length=300, null=True, verbose_name='औपचारिक शैक्षिक योग्यता')),
                ('subject', models.CharField(blank=True, max_length=300, null=True, verbose_name='बिषय')),
                ('permanent_address', models.CharField(blank=True, max_length=300, null=True, verbose_name='ठेगाना(स्थायी): जिल्ला')),
                ('permanent_gapa_napa', models.CharField(blank=True, max_length=300, null=True, verbose_name='गाउँपालिका/नगरपालिका/उप-महानगरपालिका/महानगरपालिका')),
                ('permanent_ward_no', models.CharField(blank=True, max_length=300, verbose_name='वडा नं')),
                ('permanent_tole', models.CharField(blank=True, max_length=300, verbose_name='टोल')),
                ('temporary_address', models.CharField(blank=True, max_length=300, verbose_name='ठेगाना(अस्थायी): जिल्ला')),
                ('temporary_gapa_napa', models.CharField(blank=True, max_length=300, verbose_name='गाउँपालिका/नगरपालिका/उप-महानगरपालिका/महानगरपालिका')),
                ('temporary_ward_no', models.CharField(blank=True, max_length=300, verbose_name='वडा नं')),
                ('temporary_tole', models.CharField(blank=True, max_length=300, verbose_name='टोल')),
                ('mobile', models.CharField(blank=True, max_length=300, verbose_name='मोवाइल')),
                ('contact_number', models.CharField(blank=True, max_length=300, verbose_name='सम्पर्क न.')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='इ-मेल')),
                ('social_networking_medium', models.CharField(blank=True, max_length=300, verbose_name='सामाजिक सन्जालका माध्यम(छ भने):')),
                ('nirwachit_prakriya', models.CharField(blank=True, max_length=300, null=True, verbose_name='निर्वाचित प्रक्रिया')),
                ('updated_nirwachit_prakriya', models.CharField(blank=True, choices=[('समानुपातिक', 'समानुपातिक'), ('प्रतक्ष्य', 'प्रतक्ष्य')], max_length=300, null=True, verbose_name='निर्वाचित प्रक्रिया')),
                ('nirwachit_padh', models.CharField(blank=True, max_length=300, verbose_name='निर्वाचित पद')),
                ('updated_nirwachit_padh', models.CharField(blank=True, choices=[('सांसद - प्रदेशसभा', 'सांसद - प्रदेशसभा')], max_length=300, null=True, verbose_name='निर्वाचित पद')),
                ('pichidiyeko_chhetra_ho_hoina', models.CharField(blank=True, max_length=300, null=True, verbose_name='पिछडिएको क्षेत्र हो कि होइन')),
                ('updated_pichidiyeko_chhetra_ho_hoina', models.CharField(blank=True, choices=[('हो', 'हो'), ('होइन', 'होइन')], max_length=300, null=True, verbose_name='पिछडिएको क्षेत्र हो कि होइन')),
                ('nirwachit_chhetrako_bibaran', models.CharField(blank=True, max_length=300, verbose_name='निर्वाचित क्षेत्रको विवरण')),
                ('nirwachit_vayeko_chhetra_aafno_thegana', models.CharField(blank=True, max_length=300, null=True, verbose_name='निर्वाचित भएको क्षेत्र आफ्नो अस्थायी/ स्थायी ठेगाना भन्दा फरक')),
                ('updated_nirwachit_vayeko_chhetra_aafno_thegana', models.CharField(blank=True, choices=[('हो', 'हो'), ('होइन', 'होइन')], max_length=300, null=True, verbose_name='निर्वाचित भएको क्षेत्र आफ्नो अस्थायी/ स्थायी ठेगाना भन्दा फरक')),
                ('party_name', models.CharField(blank=True, max_length=300, verbose_name='पार्टीको विवरण: पार्टीको नाम')),
                ('party_joined_date', models.CharField(blank=True, max_length=300, null=True, verbose_name='पार्टीमा संलग्न भएको मिति')),
                ('pramukh_jimmewari', models.CharField(blank=True, max_length=300, verbose_name='प्रमुख जिम्मेवारी ')),
                ('nirwachit_chetra_pratiko_pratibadhata', models.TextField(blank=True, null=True, verbose_name='निर्वाचित क्षेत्र प्रतिको प्रतिबध्धता')),
                ('aaja_vanda_agadi_chunab_ladnu_vayeko_chha', models.CharField(blank=True, max_length=300, null=True, verbose_name='आज भन्दा अघि चुनाब लड्नुभएको छ?')),
                ('updated_aaja_vanda_agadi_chunab_ladnu_vayeko_chha', models.CharField(blank=True, choices=[('समानुपातिक', 'समानुपातिक'), ('छैन', 'छैन'), ('छ', 'छ')], max_length=300, null=True, verbose_name='आज भन्दा अघि चुनाब लड्नुभएको छ?')),
                ('prapta_maat_sankhya', models.CharField(blank=True, max_length=300, verbose_name='प्राप्त मत संख्या')),
                ('samlagna_sang_sastha_samuha', models.CharField(blank=True, max_length=300, verbose_name='सलग्न संघ, सस्था , समूह')),
                ('status', models.BooleanField(choices=[(True, 'पूर्ण'), (False, 'अपूर्ण')], default=False, verbose_name='स्थिति')),
                ('image', models.ImageField(blank=True, null=True, upload_to='provinceProfile/', verbose_name='फोटो')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RastriyaShava',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='नाम')),
                ('english_name', models.CharField(max_length=300, verbose_name='English Name')),
                ('date_of_birth', models.CharField(max_length=300, verbose_name='जन्ममिती')),
                ('mothers_name', models.CharField(max_length=300, verbose_name='आमाको नाम')),
                ('fathers_name', models.CharField(max_length=300, verbose_name='बाबुको नाम')),
                ('marital_status', models.CharField(blank=True, max_length=300, null=True, verbose_name='बैवाहिक स्थिथि')),
                ('updated_marital_status', models.CharField(blank=True, choices=[('cljjflxt', 'अविवाहित'), ('ljjflxt', 'विवाहित'), ('Psn', 'एकल'), ('cGo', 'अन्य')], max_length=300, null=True, verbose_name='बैवाहिक स्थिथि')),
                ('husbands_name', models.CharField(max_length=300, verbose_name='श्रीमानको नाम')),
                ('caste', models.CharField(blank=True, max_length=300, null=True, verbose_name='जातियता')),
                ('updated_caste', models.CharField(blank=True, choices=[('blnt', 'दलित'), ('cflbaf;L÷hghftL', 'आदिबासी / जनजाती'), ('v; cfo{', 'खस आर्य'), ('dw];L ', 'मधेसी'), ('yf?', 'थारु'), ('d"l:nd', 'मुस्लिम'), ('cGo', 'अन्य')], max_length=300, null=True, verbose_name='जातियता')),
                ('mother_tongue', models.CharField(blank=True, max_length=300, null=True, verbose_name='मातृभाषा')),
                ('updated_mother_tongue', models.CharField(blank=True, choices=[('नेपाली', 'नेपाली'), ('मगर खामस्तानाकोतरराजनीति शास्त्र', 'मगर खामस्तानाकोतरराजनीति शास्त्र'), ('नेवारी', 'नेवारी'), ('नेपाल भाषा', 'नेपाल भाषा'), ('तामाङ', 'तामाङ')], max_length=300, null=True, verbose_name='मातृभाषा')),
                ('educational_qualification', models.CharField(blank=True, max_length=300, null=True, verbose_name='औपचारिक शैक्षिक योग्यता')),
                ('updated_educational_qualification', models.CharField(blank=True, choices=[('lg/If/', 'निरक्षर'), (';fIf/', 'साक्षर'), ('P;=Pn=;L= ', 'एस.एल.सी.'), ('!) @ jf ;f] ;/x', '१० + २ वा सो सरह'), (':gfts', 'स्नातक'), (':gfsf]]t/', 'स्नाकोतर'), ('lk=Pr=8L=', 'पि.एच.डी')], max_length=300, null=True, verbose_name='औपचारिक शैक्षिक योग्यता')),
                ('subject', models.CharField(blank=True, max_length=300, null=True, verbose_name='बिषय')),
                ('permanent_address', models.CharField(blank=True, max_length=300, null=True, verbose_name='ठेगाना(स्थायी): जिल्ला')),
                ('permanent_gapa_napa', models.CharField(blank=True, max_length=300, null=True, verbose_name='गाउँपालिका/नगरपालिका/उप-महानगरपालिका/महानगरपालिका')),
                ('permanent_ward_no', models.CharField(blank=True, max_length=300, verbose_name='वडा नं')),
                ('permanent_tole', models.CharField(blank=True, max_length=300, verbose_name='टोल')),
                ('temporary_address', models.CharField(blank=True, max_length=300, verbose_name='ठेगाना(अस्थायी): जिल्ला')),
                ('temporary_gapa_napa', models.CharField(blank=True, max_length=300, verbose_name='गाउँपालिका/नगरपालिका/उप-महानगरपालिका/महानगरपालिका')),
                ('temporary_ward_no', models.CharField(blank=True, max_length=300, verbose_name='वडा नं')),
                ('temporary_tole', models.CharField(blank=True, max_length=300, verbose_name='टोल')),
                ('mobile', models.CharField(blank=True, max_length=300, verbose_name='मोवाइल')),
                ('contact_number', models.CharField(blank=True, max_length=300, verbose_name='सम्पर्क न.')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='इ-मेल')),
                ('social_networking_medium', models.CharField(blank=True, max_length=300, verbose_name='सामाजिक सन्जालका माध्यम(छ भने):')),
                ('nirwachit_prakriya', models.CharField(blank=True, max_length=300, null=True, verbose_name='निर्वाचित प्रक्रिया')),
                ('updated_nirwachit_prakriya', models.CharField(blank=True, choices=[('समानुपातिक', 'समानुपातिक'), ('प्रतक्ष्य', 'प्रतक्ष्य')], max_length=300, null=True, verbose_name='निर्वाचित प्रक्रिया')),
                ('nirwachit_padh', models.CharField(blank=True, max_length=300, verbose_name='निर्वाचित पद')),
                ('updated_nirwachit_padh', models.CharField(blank=True, choices=[('सांसद - प्रदेशसभा', 'सांसद - प्रदेशसभा')], max_length=300, null=True, verbose_name='निर्वाचित पद')),
                ('pichidiyeko_chhetra_ho_hoina', models.CharField(blank=True, max_length=300, null=True, verbose_name='पिछडिएको क्षेत्र हो कि होइन')),
                ('updated_pichidiyeko_chhetra_ho_hoina', models.CharField(blank=True, choices=[('हो', 'हो'), ('होइन', 'होइन')], max_length=300, null=True, verbose_name='पिछडिएको क्षेत्र हो कि होइन')),
                ('nirwachit_chhetrako_bibaran', models.CharField(blank=True, max_length=300, verbose_name='निर्वाचित क्षेत्रको विवरण')),
                ('nirwachit_vayeko_chhetra_aafno_thegana', models.CharField(blank=True, max_length=300, null=True, verbose_name='निर्वाचित भएको क्षेत्र आफ्नो अस्थायी/ स्थायी ठेगाना भन्दा फरक')),
                ('updated_nirwachit_vayeko_chhetra_aafno_thegana', models.CharField(blank=True, choices=[('हो', 'हो'), ('होइन', 'होइन')], max_length=300, null=True, verbose_name='निर्वाचित भएको क्षेत्र आफ्नो अस्थायी/ स्थायी ठेगाना भन्दा फरक')),
                ('party_name', models.CharField(blank=True, max_length=300, verbose_name='पार्टीको विवरण: पार्टीको नाम')),
                ('party_joined_date', models.CharField(blank=True, max_length=300, null=True, verbose_name='पार्टीमा संलग्न भएको मिति')),
                ('pramukh_jimmewari', models.CharField(blank=True, max_length=300, verbose_name='प्रमुख जिम्मेवारी ')),
                ('nirwachit_chetra_pratiko_pratibadhata', models.TextField(blank=True, null=True, verbose_name='निर्वाचित क्षेत्र प्रतिको प्रतिबध्धता')),
                ('aaja_vanda_agadi_chunab_ladnu_vayeko_chha', models.CharField(blank=True, max_length=300, null=True, verbose_name='आज भन्दा अघि चुनाब लड्नुभएको छ?')),
                ('updated_aaja_vanda_agadi_chunab_ladnu_vayeko_chha', models.CharField(blank=True, choices=[('समानुपातिक', 'समानुपातिक'), ('छैन', 'छैन'), ('छ', 'छ')], max_length=300, null=True, verbose_name='आज भन्दा अघि चुनाब लड्नुभएको छ?')),
                ('prapta_maat_sankhya', models.CharField(blank=True, max_length=300, verbose_name='प्राप्त मत संख्या')),
                ('samlagna_sang_sastha_samuha', models.CharField(blank=True, max_length=300, verbose_name='सलग्न संघ, सस्था , समूह')),
                ('status', models.BooleanField(choices=[(True, 'पूर्ण'), (False, 'अपूर्ण')], default=False, verbose_name='स्थिति')),
                ('image', models.ImageField(blank=True, null=True, upload_to='provinceProfile/', verbose_name='फोटो')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]