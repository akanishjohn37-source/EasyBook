-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 23, 2024 at 07:56 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `easy_book_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add author', 7, 'add_author'),
(26, 'Can change author', 7, 'change_author'),
(27, 'Can delete author', 7, 'delete_author'),
(28, 'Can view author', 7, 'view_author'),
(29, 'Can add author_book', 8, 'add_author_book'),
(30, 'Can change author_book', 8, 'change_author_book'),
(31, 'Can delete author_book', 8, 'delete_author_book'),
(32, 'Can view author_book', 8, 'view_author_book'),
(33, 'Can add book', 9, 'add_book'),
(34, 'Can change book', 9, 'change_book'),
(35, 'Can delete book', 9, 'delete_book'),
(36, 'Can view book', 9, 'view_book'),
(37, 'Can add category', 10, 'add_category'),
(38, 'Can change category', 10, 'change_category'),
(39, 'Can delete category', 10, 'delete_category'),
(40, 'Can view category', 10, 'view_category'),
(41, 'Can add complaint', 11, 'add_complaint'),
(42, 'Can change complaint', 11, 'change_complaint'),
(43, 'Can delete complaint', 11, 'delete_complaint'),
(44, 'Can view complaint', 11, 'view_complaint'),
(45, 'Can add feedback', 12, 'add_feedback'),
(46, 'Can change feedback', 12, 'change_feedback'),
(47, 'Can delete feedback', 12, 'delete_feedback'),
(48, 'Can view feedback', 12, 'view_feedback'),
(49, 'Can add language', 13, 'add_language'),
(50, 'Can change language', 13, 'change_language'),
(51, 'Can delete language', 13, 'delete_language'),
(52, 'Can view language', 13, 'view_language'),
(53, 'Can add login', 14, 'add_login'),
(54, 'Can change login', 14, 'change_login'),
(55, 'Can delete login', 14, 'delete_login'),
(56, 'Can view login', 14, 'view_login'),
(57, 'Can add membership_amount', 15, 'add_membership_amount'),
(58, 'Can change membership_amount', 15, 'change_membership_amount'),
(59, 'Can delete membership_amount', 15, 'delete_membership_amount'),
(60, 'Can view membership_amount', 15, 'view_membership_amount'),
(61, 'Can add order', 16, 'add_order'),
(62, 'Can change order', 16, 'change_order'),
(63, 'Can delete order', 16, 'delete_order'),
(64, 'Can view order', 16, 'view_order'),
(65, 'Can add user_register', 17, 'add_user_register'),
(66, 'Can change user_register', 17, 'change_user_register'),
(67, 'Can delete user_register', 17, 'delete_user_register'),
(68, 'Can view user_register', 17, 'view_user_register'),
(69, 'Can add author_name', 18, 'add_author_name'),
(70, 'Can change author_name', 18, 'change_author_name'),
(71, 'Can delete author_name', 18, 'delete_author_name'),
(72, 'Can view author_name', 18, 'view_author_name'),
(73, 'Can add fee', 19, 'add_fee'),
(74, 'Can change fee', 19, 'change_fee'),
(75, 'Can delete fee', 19, 'delete_fee'),
(76, 'Can view fee', 19, 'view_fee');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$0LFFXAQ7IYDKoLFrQw85wp$ppN6owBiSn4z6B90GNtwdIpigakmW7bKT7zwkYpxC28=', NULL, 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2024-02-20 08:23:11.825737');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'bookapp', 'author'),
(8, 'bookapp', 'author_book'),
(18, 'bookapp', 'author_name'),
(9, 'bookapp', 'book'),
(10, 'bookapp', 'category'),
(11, 'bookapp', 'complaint'),
(19, 'bookapp', 'fee'),
(12, 'bookapp', 'feedback'),
(13, 'bookapp', 'language'),
(14, 'bookapp', 'login'),
(15, 'bookapp', 'membership_amount'),
(16, 'bookapp', 'order'),
(17, 'bookapp', 'user_register'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-02-19 09:20:55.969302'),
(2, 'auth', '0001_initial', '2024-02-19 09:20:56.408377'),
(3, 'admin', '0001_initial', '2024-02-19 09:20:56.517778'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-02-19 09:20:56.517778'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-02-19 09:20:56.533401'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-02-19 09:20:56.612116'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-02-19 09:20:56.659458'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-02-19 09:20:56.675090'),
(9, 'auth', '0004_alter_user_username_opts', '2024-02-19 09:20:56.675090'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-02-19 09:20:56.737589'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-02-19 09:20:56.737589'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-02-19 09:20:56.754721'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-02-19 09:20:56.754721'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-02-19 09:20:56.769229'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-02-19 09:20:56.784863'),
(16, 'auth', '0011_update_proxy_permissions', '2024-02-19 09:20:56.784863'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-02-19 09:20:56.800487'),
(18, 'bookapp', '0001_initial', '2024-02-19 09:20:56.879046'),
(19, 'sessions', '0001_initial', '2024-02-19 09:20:56.910262'),
(20, 'bookapp', '0002_author_name', '2024-02-20 12:25:28.070202'),
(21, 'bookapp', '0003_alter_book_doc_alter_book_type', '2024-02-21 06:37:57.869878'),
(22, 'bookapp', '0004_alter_book_quantity', '2024-02-21 06:47:27.259188'),
(23, 'bookapp', '0005_alter_order_check_no_order_alter_order_quantity', '2024-02-22 09:32:58.912231'),
(24, 'bookapp', '0006_book_user_type', '2024-02-22 16:59:30.701436'),
(25, 'bookapp', '0007_book_status', '2024-02-23 08:59:21.584487'),
(26, 'bookapp', '0008_fee', '2024-02-23 13:17:47.847387'),
(27, 'bookapp', '0009_delete_author_book_author_expiry_date', '2024-02-23 17:42:25.953981');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('e3gbqurtbqqes3bsra89nrq1cbvmsvnl', 'eyJhdW5hbWUiOiJqYW1lczEyMyIsInNsb2dpZCI6M30:1rdZAW:wFz3UfahHM0sJTQR-thkeMwuyyX53Lw6zzA68BtrlKk', '2024-03-08 17:17:04.873422'),
('zkrddlqty263fh8xt1givaw70o025wt7', 'eyJ1bmFtZSI6ImNoaW5udTEyMyIsInNsb2dpZCI6MX0:1rckgA:gEKTPPSiA9w7H5L3ZTOOObml8MBdVJK0bI0cAiujDVY', '2024-03-06 11:22:22.317142');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_author`
--

CREATE TABLE `tbl_author` (
  `author_id` int(11) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `address` longtext NOT NULL,
  `email_id` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `phone_number` bigint(20) DEFAULT NULL,
  `photo` varchar(50) NOT NULL,
  `login_id` int(11) NOT NULL,
  `membership` varchar(50) NOT NULL,
  `expiry_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_author`
--

INSERT INTO `tbl_author` (`author_id`, `firstname`, `lastname`, `address`, `email_id`, `gender`, `phone_number`, `photo`, `login_id`, `membership`, `expiry_date`) VALUES
(1, 'james', 'John', 'James Villa', 'james@gmail.com', 'Female', 9885695441, '/media/1..jpg', 3, 'Member', '2025-02-24'),
(2, 'shenoy', 'John', 'ShenoyVilla', 'shenoy@gmail.com', 'Female', 9835346346, '/media/2..jpg', 4, 'Not Member', NULL),
(3, 'bino', 'John', 'Bino Villa', 'bino@gmail.com', 'Female', 3245346346, '/media/3..jpg', 5, 'Not Member', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_author_name`
--

CREATE TABLE `tbl_author_name` (
  `author_id` int(11) NOT NULL,
  `author` varchar(50) NOT NULL,
  `about_author` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_author_name`
--

INSERT INTO `tbl_author_name` (`author_id`, `author`, `about_author`) VALUES
(1, 'Rabindranath Tagor', 'Rabindranath Tagor FRAS was a Bengali polymath who was active as a poet, writer, playwright, composer, philosopher, social reformer, educationis');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_book`
--

CREATE TABLE `tbl_book` (
  `book_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `type` varchar(50) NOT NULL,
  `book_name` varchar(50) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `price` decimal(12,2) DEFAULT NULL,
  `doc` varchar(50) DEFAULT NULL,
  `image` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `user_type` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_book`
--

INSERT INTO `tbl_book` (`book_id`, `category_id`, `author_id`, `language_id`, `type`, `book_name`, `quantity`, `price`, `doc`, `image`, `description`, `user_type`, `status`) VALUES
(1, 2, 1, 1, 'Physical Book', 'Full poem and Story4', 73, 100.00, '/media/14..pdf', '/media/32..jpg', 'Rabindranath Tagore FRAS was a Bengali polymath who was active as a poet, writer, playwright, composer, philosopher, social reformer, educationist and painter during the age of Bengal Renaissance.', 'Admin', 'Approved'),
(3, 2, 1, 1, 'Journals', 'gj', NULL, 300.00, '/media/24..pdf', '/media/23..jpg', 'hjghj', 'Admin', 'Approved'),
(4, 2, 1, 1, 'E-Book', 'Full poem and Story1', NULL, 300.00, '/media/26..pdf', '/media/25..jpg', 'erwerer', 'Admin', 'Approved'),
(5, 2, 3, 1, 'Physical Book', 'Full poem and Story2', 1, 3000.00, NULL, '/media/35..jpg', '1A special 30th anniversary edition of the extraordinary international bestseller, with a new foreword.Every few decades a book is published that changes the lives of its readers forever. This is such a book – a beautiful parable about learning to listen to your heart, read the omens strewn along life’s path and, above all, follow your dreams.Santiago, a young shepherd living in the hills of Andalucia, feels that there is more to life than his humble home and his flock. One day he finds the courage to follow his dreams into distant lands, each step galvanised by the knowledge that he is following the right path: his own. The people he meets along the way, the things he sees and the wisdom he learns are life-changing.With Paulo Coelho’s visionary blend of spirituality, magical realism and folklore, The Alchemist is a story with the power to inspire nations and change people’s lives.', 'Author', 'Approved'),
(6, 2, 3, 1, 'E-Book', 'The Law of Success', NULL, 1000.00, '/media/37..pdf', '/media/36..jpg', '“Fears are nothing more than a state of mind.”From helping you rid yourself of aimlessness and find a definite purpose to teaching you the art of negotiating harmoniously with others, this course on the fundamentals of success will guide you, lesson by lesson, through the sixteen laws of success, which include mastering fears and increasing self-confidence, inculcating the habit of saving your income, stimulating your imagination, practicing self-control, accurate thinking and profiting by failure. With valuable insights on how the famous American millionaires became successful, Napoleon Hill’s The Law of Success in Sixteen Lessons is a classic bestseller. It continues to inspire and guide readers to achieve their dreams and become successful.', 'Author', 'Rejected');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_category`
--

CREATE TABLE `tbl_category` (
  `category_id` int(11) NOT NULL,
  `category` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_category`
--

INSERT INTO `tbl_category` (`category_id`, `category`) VALUES
(1, 'Classic'),
(2, 'Scientific'),
(3, 'Fiction'),
(4, 'Medicine'),
(5, 'Law');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_complaint`
--

CREATE TABLE `tbl_complaint` (
  `complaint_id` int(11) NOT NULL,
  `complaint_subject` varchar(50) NOT NULL,
  `complaint` varchar(150) NOT NULL,
  `user_login_id` int(11) NOT NULL,
  `reply` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_complaint`
--

INSERT INTO `tbl_complaint` (`complaint_id`, `complaint_subject`, `complaint`, `user_login_id`, `reply`) VALUES
(1, 'gdf', 'dfgdf', 1, 'yes');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_customer_register`
--

CREATE TABLE `tbl_customer_register` (
  `user_id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `phone_number` bigint(20) DEFAULT NULL,
  `Email` varchar(50) NOT NULL,
  `Address` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_customer_register`
--

INSERT INTO `tbl_customer_register` (`user_id`, `login_id`, `Name`, `phone_number`, `Email`, `Address`) VALUES
(1, 1, 'Chinnu', 7485963625, 'chinnu@gmail.com', 'Chinnu Villa');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_fee`
--

CREATE TABLE `tbl_fee` (
  `fee_id` int(11) NOT NULL,
  `fee` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_fee`
--

INSERT INTO `tbl_fee` (`fee_id`, `fee`) VALUES
(1, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_feedback`
--

CREATE TABLE `tbl_feedback` (
  `feedback_id` int(11) NOT NULL,
  `feedback_subject` varchar(50) NOT NULL,
  `feedback` longtext NOT NULL,
  `user_login_id` int(11) NOT NULL,
  `reply` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_feedback`
--

INSERT INTO `tbl_feedback` (`feedback_id`, `feedback_subject`, `feedback`, `user_login_id`, `reply`) VALUES
(1, 'Hello', 'hello', 1, 'okay');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_language`
--

CREATE TABLE `tbl_language` (
  `language_id` int(11) NOT NULL,
  `language` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_language`
--

INSERT INTO `tbl_language` (`language_id`, `language`) VALUES
(1, 'English'),
(2, 'Hindi'),
(3, 'Tamil'),
(4, 'Urdu');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_login`
--

CREATE TABLE `tbl_login` (
  `login_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` longtext DEFAULT NULL,
  `Usertype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_login`
--

INSERT INTO `tbl_login` (`login_id`, `username`, `password`, `Usertype`, `status`) VALUES
(1, 'chinnu123', 'chinnu123', 'User', 'Approved'),
(3, 'james123', 'james123', 'Author', 'Approved'),
(4, 'shenoy123', 'shenoy123', 'Author', 'Approved'),
(5, 'bino123', 'bino123', 'Author', 'Approved');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_membership_amount`
--

CREATE TABLE `tbl_membership_amount` (
  `membership_amount_id` int(11) NOT NULL,
  `amount` decimal(12,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_order`
--

CREATE TABLE `tbl_order` (
  `order_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `amount` decimal(12,2) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `entry_date` datetime(6) NOT NULL,
  `user_login_id` int(11) NOT NULL,
  `check_no_order` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_order`
--

INSERT INTO `tbl_order` (`order_id`, `book_id`, `amount`, `quantity`, `status`, `entry_date`, `user_login_id`, `check_no_order`) VALUES
(1, 3, 300.00, NULL, 'Not Paid', '2024-02-22 15:03:06.859482', 1, NULL),
(2, 3, 300.00, NULL, 'Not Paid', '2024-02-22 15:03:58.238984', 1, NULL),
(3, 3, 300.00, NULL, 'Not Paid', '2024-02-22 15:04:51.256273', 1, NULL),
(4, 3, 300.00, NULL, 'Not Paid', '2024-02-22 15:16:05.236003', 1, NULL),
(5, 3, 300.00, NULL, 'Delivered', '2024-02-22 15:16:35.511584', 1, NULL),
(6, 3, 300.00, NULL, 'Paid', '2024-02-22 15:17:04.855746', 1, NULL),
(7, 3, 300.00, NULL, 'Not Paid', '2024-02-22 15:17:17.125972', 1, NULL),
(8, 3, 300.00, NULL, 'Not Paid', '2024-02-22 15:17:26.651582', 1, NULL),
(9, 4, 300.00, NULL, 'Paid', '2024-02-22 15:20:55.359612', 1, NULL),
(10, 3, 300.00, NULL, 'Paid', '2024-02-22 15:21:56.189846', 1, NULL),
(11, 1, 900.00, 9, 'Not Paid', '2024-02-22 16:35:13.804715', 1, 372816),
(12, 3, 900.00, 9, 'Not Paid', '2024-02-22 16:35:13.895239', 1, 372816),
(13, 1, 100.00, 1, 'Not Paid', '2024-02-22 16:35:39.239077', 1, 236001),
(14, 1, 200.00, 2, 'Paid', '2024-02-22 17:27:11.160628', 1, 689487),
(15, 3, 300.00, NULL, 'Not Paid', '2024-02-23 15:49:50.473466', 1, NULL),
(16, 6, 1000.00, NULL, 'Not Paid', '2024-02-23 15:54:46.616749', 1, NULL),
(17, 1, 100.00, 1, 'Not Paid', '2024-02-23 16:06:02.281438', 1, 50498),
(18, 3, 300.00, NULL, 'Not Paid', '2024-02-23 16:06:21.630527', 1, NULL),
(19, 6, 1000.00, NULL, 'Not Paid', '2024-02-23 17:25:59.966222', 1, NULL),
(20, 5, 6000.00, 2, 'Delivered', '2024-02-23 17:28:05.385189', 1, 689614),
(21, 1, 200.00, 2, 'Paid', '2024-02-23 17:28:05.397491', 1, 689614),
(22, 6, 1000.00, NULL, 'Paid', '2024-02-23 17:28:50.837140', 1, NULL),
(23, 6, 1000.00, NULL, 'Not Paid', '2024-02-23 17:39:10.782492', 1, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `tbl_author`
--
ALTER TABLE `tbl_author`
  ADD PRIMARY KEY (`author_id`);

--
-- Indexes for table `tbl_author_name`
--
ALTER TABLE `tbl_author_name`
  ADD PRIMARY KEY (`author_id`);

--
-- Indexes for table `tbl_book`
--
ALTER TABLE `tbl_book`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `tbl_category`
--
ALTER TABLE `tbl_category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `tbl_complaint`
--
ALTER TABLE `tbl_complaint`
  ADD PRIMARY KEY (`complaint_id`);

--
-- Indexes for table `tbl_customer_register`
--
ALTER TABLE `tbl_customer_register`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `tbl_fee`
--
ALTER TABLE `tbl_fee`
  ADD PRIMARY KEY (`fee_id`);

--
-- Indexes for table `tbl_feedback`
--
ALTER TABLE `tbl_feedback`
  ADD PRIMARY KEY (`feedback_id`);

--
-- Indexes for table `tbl_language`
--
ALTER TABLE `tbl_language`
  ADD PRIMARY KEY (`language_id`);

--
-- Indexes for table `tbl_login`
--
ALTER TABLE `tbl_login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `tbl_membership_amount`
--
ALTER TABLE `tbl_membership_amount`
  ADD PRIMARY KEY (`membership_amount_id`);

--
-- Indexes for table `tbl_order`
--
ALTER TABLE `tbl_order`
  ADD PRIMARY KEY (`order_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `tbl_author`
--
ALTER TABLE `tbl_author`
  MODIFY `author_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_author_name`
--
ALTER TABLE `tbl_author_name`
  MODIFY `author_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_book`
--
ALTER TABLE `tbl_book`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tbl_category`
--
ALTER TABLE `tbl_category`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_complaint`
--
ALTER TABLE `tbl_complaint`
  MODIFY `complaint_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_customer_register`
--
ALTER TABLE `tbl_customer_register`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_fee`
--
ALTER TABLE `tbl_fee`
  MODIFY `fee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_feedback`
--
ALTER TABLE `tbl_feedback`
  MODIFY `feedback_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_language`
--
ALTER TABLE `tbl_language`
  MODIFY `language_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_login`
--
ALTER TABLE `tbl_login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tbl_membership_amount`
--
ALTER TABLE `tbl_membership_amount`
  MODIFY `membership_amount_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_order`
--
ALTER TABLE `tbl_order`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
