"""Utility for loading and validating exercise templates."""
import yaml
from pathlib import Path
from typing import Dict, List, Any
from .exceptions import FileOperationError
from .logger import logger

class TemplateLoader:
    """Handles loading and validating exercise templates."""
    
    def __init__(self, template_dir: str = "templates"):
        """Initialize the template loader.
        
        Args:
            template_dir: Directory containing template files
        """
        self.template_dir = Path(template_dir)
        
    def load_yaml_template(self, template_name: str) -> Dict[str, Any]:
        """Load a YAML template file.
        
        Args:
            template_name: Name of the template file (without extension)
            
        Returns:
            Dict containing the template data
            
        Raises:
            FileOperationError: If template cannot be loaded
        """
        try:
            template_path = self.template_dir / f"{template_name}.yaml"
            if not template_path.exists():
                raise FileOperationError(f"Template file not found: {template_name}.yaml")
                
            with template_path.open('r', encoding='utf-8') as f:
                template = yaml.safe_load(f)
                
            self._validate_template(template)
            logger.info(f"Successfully loaded template: {template_name}")
            return template
            
        except Exception as e:
            logger.error(f"Failed to load template {template_name}: {str(e)}")
            raise FileOperationError(f"Could not load template: {str(e)}") from e
            
    def _validate_template(self, template: Dict[str, Any]) -> None:
        """Validate the structure of a loaded template.
        
        Args:
            template: Template data to validate
            
        Raises:
            ValueError: If template structure is invalid
        """
        required_fields = ['name', 'type', 'settings', 'prompts']
        for field in required_fields:
            if field not in template:
                raise ValueError(f"Missing required field: {field}")
                
        settings = template['settings']
        required_settings = ['responses_per_prompt', 'days_per_week', 'total_weeks']
        for setting in required_settings:
            if setting not in settings:
                raise ValueError(f"Missing required setting: {setting}")
                
        if 'assessment' not in template:
            raise ValueError("Missing assessment configuration")
            
    def get_week_prompts(self, template: Dict[str, Any], week: int) -> List[str]:
        """Get prompts for a specific week.
        
        Args:
            template: Loaded template data
            week: Week number (1-based)
            
        Returns:
            List of prompts for the week
            
        Raises:
            ValueError: If week number is invalid
        """
        if not 1 <= week <= template['settings']['total_weeks']:
            raise ValueError(f"Week must be between 1 and {template['settings']['total_weeks']}")
            
        week_key = f"week{week}"
        prompts = template['prompts'].get(week_key, [])
        
        if not prompts:
            logger.warning(f"No prompts found for {week_key}")
            
        return prompts
        
    def get_assessment_config(self, template: Dict[str, Any]) -> Dict[str, Any]:
        """Get assessment configuration from template.
        
        Args:
            template: Loaded template data
            
        Returns:
            Assessment configuration
        """
        return template['assessment'] 