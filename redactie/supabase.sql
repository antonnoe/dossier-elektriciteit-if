-- Redactieopmerkingen — eenmalig uitvoeren in de Supabase SQL-editor (project naar keuze, bv. DossierFrankrijk Pro)
create table if not exists public.redactie_opmerkingen (
  id uuid primary key default gen_random_uuid(),
  dossier text not null,
  blok text not null,
  hoofdstuk text,
  fragment text,
  opmerking text not null,
  created_at timestamptz not null default now()
);
alter table public.redactie_opmerkingen enable row level security;
-- alleen toevoegen met de publieke anon-sleutel; lezen kan uitsluitend via het dashboard/service-rol
create policy "anon mag opmerkingen toevoegen" on public.redactie_opmerkingen
  for insert to anon with check (true);
-- bewust GEEN select/update/delete-policy voor anon
