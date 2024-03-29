﻿using E_Commerce.Data.Base;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace E_Commerce.Models
{
    public class Producer : IEntityBase
    {

        [Key]
        public int Id { get; set; }
        [Display (Name="Profile Picture URL")]
        public string ProfilePictureURL { get; set; }

        [Display (Name = "Full Name")]
        public string FullName { get; set; }
        [Display (Name="Biography")]
        public string Bio { get; set; }

        //Relationships
        public List<Movie> Movies { get; set; }
    }
}
