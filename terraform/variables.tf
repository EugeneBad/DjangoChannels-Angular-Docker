variable "service-account-file" {
  description = "The path to the project service account file"
}

variable "gce-ssh-user" {
  description = "User the provisioning stage uses."
}

variable "gce-ssh-pub-key-file" {
  description = "gce-ssh-user public key file"
}

variable "gce-ssh-private-key-file" {
  description = "gce-ssh-user private key file"
}

variable "k8scluster-join-hash" {}