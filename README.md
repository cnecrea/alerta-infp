# Alerta INFP - Home Assistant Custom Component

![Project Status](https://img.shields.io/badge/status-active-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![HACS Supported](https://img.shields.io/badge/HACS-Supported-orange)

Monitorizează alertele seismice de pe site-ul INFP (Institutul Național de Fizică a Pământului) direct în Home Assistant.

## Caracteristici
- **Monitorizare automată:** Verifică site-ul INFP la intervale regulate.
- **Statut în timp real:** Informează despre activitatea seismică și starea site-ului INFP.
- **Senzori adiționali:** Include timp de răspuns al serverului și numărul de alerte detectate.
- **Notificări și entități native:** Se integrează perfect cu Home Assistant.

---

## Instalare

### Manual
1. Descarcă acest repository și copiază folderul `alerta_infp` în directorul `custom_components` din instalarea ta Home Assistant.
   - Dacă directorul `custom_components` nu există, creează-l în directorul de configurare (acolo unde se află `configuration.yaml`).
2. Repornește Home Assistant.
3. Verifică jurnalul pentru a te asigura că componenta a fost încărcată corect.

### HACS (Home Assistant Community Store)
1. Adaugă repository-ul în HACS ca **Custom Repository**:
   - Mergi la HACS > Integrations > "Custom repositories" > Adaugă URL-ul acestui repository.
2. Instalează integrarea din HACS.
3. Repornește Home Assistant.

---

## Configurare

### În `configuration.yaml` (opțional)
Dacă dorești să ajustezi intervalul de scanare, adaugă următoarele în `configuration.yaml`:

```yaml
alerta_infp:
  scan_interval: 120
