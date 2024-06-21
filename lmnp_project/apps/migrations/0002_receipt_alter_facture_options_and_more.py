# Generated by Django 4.1 on 2022-11-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_type', models.CharField(blank=True, choices=[('loyers_hors_charges', 'Loyers - Loyer hors charges locatives'), ('loyers_ct', 'Loyers - Loyer court terme (AirBnb...)'), ('provision_charges', 'Charges locatives - Provision pour charges'), ('regularisation_charges', 'Charges locatives - Régularisation des charges'), ('forfait_charges', 'Charges locatives - Forfait pour charges'), ('menage', 'Charges locatives - Ménage'), ('recuperation_tom', 'Charges locatives - Récupération de la TOM'), ('depot_garantie', 'Autres recettes - Dépôt de garantie versé par le locataire'), ('retenue_depot_garantie', 'Autres recettes - Retenue sur le dépôt de garantie'), ('assurance_loyer_impaye', 'Autres recettes - Indemnité assurance loyer impayé'), ('assurance_sinistre', 'Autres recettes - Indemnité assurance sinistre'), ('assurance_emprunteur', 'Autres recettes - Indemnité assurance emprunteur'), ('remboursement_honoraire_notaire', 'Autres recettes - Remboursement trop payé honoraire du notaire'), ('remboursement_fournisseur_energie', 'Autres recettes - Remboursement trop payé fournisseur énergie'), ('fond_solidarite', 'Autres recettes - Fond de solidarité COVID 19'), ('remboursement_fond_garantie (Crédit logement)', 'Autres recettes - Remboursement Fond Mutuel de Garantie (Crédit logement)'), ('plus_values', "Plus values - Cession de mobilier ou d'équipements comptabilisés en charges")], max_length=150, null=True, verbose_name='Type')),
                ('amount', models.FloatField(blank=True, null=True, verbose_name='Montant HT')),
                ('amount_ttc', models.FloatField(blank=True, null=True, verbose_name='Montant TTC')),
                ('date_receipt', models.DateField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Commentaires')),
                ('date_entered', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Recette',
                'db_table': 'receipt',
            },
        ),
        migrations.AlterModelOptions(
            name='facture',
            options={'verbose_name': 'Dépense'},
        ),
        migrations.AlterField(
            model_name='facture',
            name='date_entered',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='facture',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='facture',
            name='facture_type',
            field=models.CharField(blank=True, choices=[('eau', 'Abonnements - Eau'), ('energie', 'Abonnements - Energie'), ('internet', 'Abonnements - Internet'), ('tel', 'Abonnements - Téléphone'), ('charges_courantes', 'Charges copropriété - Charges courantes'), ('fond_prevoyance', 'Charges copropriété - Fond de prévoyance'), ('fond_roulement', 'Charges copropriété - Fond de roulement'), ('fond_travaux_alur', 'Charges copropriété - Fond Travaux ALUR'), ('travaux', 'Charges copropriété - Travaux'), ('assurance_emprunteur', 'Assurances - Assurance emprunteur'), ('assurance_pno', 'Assurances - Assurance Habitation Propriétaire Non Occupant'), ('autres_assurance', 'Assurances - Autres assurance'), ('autres_equipements', 'Equipements et entretien - Autres Equipements '), ('cuisine_equipee', 'Equipements et entretien - Cuisine équipée'), ('electromenager', 'Equipements et entretien - Electroménager'), ('entretien_reparations', 'Equipements et entretien - Entretien et réparations'), ('mobilier', 'Equipements et entretien - Mobilier'), ('travaux', 'Equipements et entretien - Travaux'), ('oga', 'Autres frais - Adhésion à un OGA'), ('amendes_circulation', 'Autres frais - Amendes de circulation'), ('autres_charges', 'Autres frais - Autres charges'), ('autres_honoraires', 'Autres frais - Autres honoraires'), ('depot_garantie', 'Autres frais - Dépôt de garantie rendu au locataire'), ('documentation', 'Autres frais - Documentation'), ('frais_bancaires', 'Autres frais - Frais bancaires'), ('frais_comptabilité', 'Autres frais - Frais de comptabilité'), ('frais_diagnostics', 'Autres frais - Frais de diagnostics'), ('frais_postaux', 'Autres frais - Frais postaux'), ('honoraires_agence', 'Autres frais - Honoraires agence (mise en relation et gestion)'), ('pub', 'Autres frais - Publicité'), ('formations', 'Autres frais - Séminaires et formations'), ('commission_garantie', 'Frais acquisition - Commission garantie (Crédit Logement)'), ('droits_mutations', 'Frais acquisition - Droits de mutations'), ('fond_mutuel_garantie', 'Frais acquisition - Fond mutuel de garantie (Crédit logement)'), ('frais_agence', 'Frais acquisition - Frais agence'), ('frais_courtage_emprunt', 'Frais acquisition - Frais de courtage emprunt'), ('honoraires_notaire', 'Frais acquisition - Honoraires du notaire'), ('assurance_vehicule', 'Frais de déplacement et de réception - Assurance véhicule'), ('carburant', 'Frais de déplacement et de réception - Carburant'), ('entretien_vehicule', 'Frais de déplacement et de réception - Entretien véhicule'), ('hebergement', 'Frais de déplacement et de réception - Hébergement'), ('location_vehicule', 'Frais de déplacement et de réception - Location de véhicule'), ('peage_parking', 'Frais de déplacement et de réception - Péage / parking'), ('restaurant', 'Frais de déplacement et de réception - Restaurant'), ('transport', 'Frais de déplacement et de réception - Train ou avion'), ('charges_sociales', 'Salaires - Charges sociales sur salaires versés'), ('salaires', 'Salaires - Salaires Versés'), ('autres_taxes', 'Impôt et taxes - Autres Impôts et taxes'), ('csg', 'Impôt et taxes - Contribution Sociale Généralisée (CSG)'), ('cfe', 'Impôt et taxes - Cotisation Foncière des Entreprises (CFE)'), ('donation_non_deductibles', 'Impôt et taxes - Droits de donation non déductibles'), ('succession_deductibles', 'Impôt et taxes - Droits de succession déductibles'), ('ir', 'Impôt et taxes - Impôt sur le revenu (IR)'), ('pfac', "Impôt et taxes - Participation pour le financement de l'assainissement collectif (PFAC)"), ('plus_value_immo', 'Impôt et taxes - Plus value immobilière'), ('redevance_tv', 'Impôt et taxes - Redevance TV'), ('taxe_amenagement', "Impôt et taxes - Taxe d'aménagement"), ('taxe_assainissement', "Impôt et taxes - Taxe d'assainissement"), ('taxe_habitation', "Impôt et taxes - Taxe d'habitation"), ('taxe_sejour', 'Impôt et taxes - Taxe de séjour'), ('teom', 'Impôt et taxes - Taxe enlèvement des ordures ménagères (TEOM)'), ('taxe_fonciere', 'Impôt et taxes - Taxe foncière'), ('taxe_petites_surfaces', 'Impôt et taxes - Taxe petites surfaces (article 234 CGI)'), ('tlv', 'Impôt et taxes - Taxe sur les logements vacants (TLV)'), ('charges_locatives', 'Sous location - Charges locatives'), ('location_immo', 'Sous location - Location immobilière')], max_length=150, null=True, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='id_facture',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]