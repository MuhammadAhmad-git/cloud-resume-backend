terraform {
  backend "s3" {
    bucket         = "muhammad-resume-2026-fra"
    key            = "backend/terraform.tfstate"
    region         = "eu-central-1"
    profile        = "Prodacc"
  }
}
